#!/usr/bin/env python3
"""Generate the reviewed SHA-256 ledger for every public file except itself."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PUBLICATION_MANIFEST.sha256"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    files = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and not path.name.startswith(".")
    )
    if any(
        path.is_symlink()
        for path in ROOT.rglob("*")
        if ".git" not in path.parts and "__pycache__" not in path.parts
    ):
        raise RuntimeError("refusing to manifest a tree containing symbolic links")
    lines = [f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}" for path in files]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"manifest_entries={len(lines)}")
    print(f"manifest_sha256={sha256(MANIFEST)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
