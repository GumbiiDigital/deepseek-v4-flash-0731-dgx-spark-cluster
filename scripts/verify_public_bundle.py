#!/usr/bin/env python3
"""Verify integrity, privacy, JSON structure, and local links for this bundle."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PUBLICATION_MANIFEST.sha256"
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".sha256"}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and not path.name.startswith(".")
    )


def verify_manifest(files: list[Path]) -> None:
    entries: dict[str, str] = {}
    for line_number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
        if not match:
            raise AssertionError(f"invalid manifest line {line_number}")
        relative = match.group(2)
        if relative.startswith("/") or ".." in Path(relative).parts or relative in entries:
            raise AssertionError(f"unsafe or duplicate manifest path at line {line_number}")
        entries[relative] = match.group(1)
    expected = {path.relative_to(ROOT).as_posix() for path in files}
    if set(entries) != expected:
        missing = sorted(expected - set(entries))
        extra = sorted(set(entries) - expected)
        raise AssertionError(f"manifest coverage failed; missing={missing}, extra={extra}")
    for relative, expected_hash in entries.items():
        path = ROOT / relative
        if not path.is_file() or path.is_symlink() or sha256(path) != expected_hash:
            raise AssertionError(f"manifest hash failed: {relative}")


def privacy_patterns() -> list[tuple[str, re.Pattern[str]]]:
    roots = [
        "/" + "Users" + "/",
        "/" + "home" + "/",
        "/" + "root" + "/",
        "." + "ssh" + "/",
        "Identity" + "File",
    ]
    return [
        ("local-root", re.compile("|".join(re.escape(value) for value in roots), re.I)),
        (
            "private-ipv4",
            re.compile(
                r"(?<![0-9])(?:10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|"
                r"192\.168\.[0-9]{1,3}\.[0-9]{1,3}|"
                r"172\.(?:1[6-9]|2[0-9]|3[01])\.[0-9]{1,3}\.[0-9]{1,3}|"
                r"100\.(?:6[4-9]|[7-9][0-9]|1[01][0-9]|12[0-7])\."
                r"[0-9]{1,3}\.[0-9]{1,3})(?![0-9])"
            ),
        ),
        ("host-identity", re.compile(r"\bspark[1-8](?:-lan|-bypass)?\b", re.I)),
        ("email", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
        (
            "secret-shape",
            re.compile(
                r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----|"
                r"AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{20,}|"
                r"hf_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|"
                r"xox[baprs]-[A-Za-z0-9-]{10,}"
            ),
        ),
        ("generated-text-field", re.compile(r'"(?:generated_texts|snippet)"\s*:')),
    ]


def verify_privacy(files: list[Path]) -> int:
    scanned = 0
    policy = ROOT / "publication-policy.json"
    for path in files:
        if path == policy or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        scanned += 1
        for identifier, pattern in privacy_patterns():
            match = pattern.search(text)
            if match:
                relative = path.relative_to(ROOT).as_posix()
                line = text.count("\n", 0, match.start()) + 1
                raise AssertionError(f"privacy check {identifier} failed at {relative}:{line}")
    return scanned


def verify_json(files: list[Path]) -> int:
    count = 0
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))
            count += 1
    return count


def verify_local_links(files: list[Path]) -> int:
    checked = 0
    for path in files:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            raw = match.group(1).strip()
            if raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw.split("#", 1)[0]
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError as exc:
                raise AssertionError(f"link escapes bundle: {path.name} -> {raw}") from exc
            if not candidate.exists():
                raise AssertionError(f"missing local link: {path.name} -> {raw}")
            checked += 1
    return checked


def main() -> int:
    files = public_files()
    if not MANIFEST.is_file():
        raise AssertionError("publication manifest is missing")
    verify_manifest(files)
    text_count = verify_privacy(files)
    json_count = verify_json(files)
    link_count = verify_local_links(files)
    if any(
        path.is_symlink()
        for path in ROOT.rglob("*")
        if ".git" not in path.parts and "__pycache__" not in path.parts
    ):
        raise AssertionError("public bundle contains a symbolic link")
    print("PUBLICATION VERIFY PASS")
    print(f"manifest_files={len(files)}")
    print(f"privacy_scanned_text_files={text_count}")
    print(f"json_files_parsed={json_count}")
    print(f"local_links_checked={link_count}")
    print(f"publication_manifest_sha256={sha256(MANIFEST)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
