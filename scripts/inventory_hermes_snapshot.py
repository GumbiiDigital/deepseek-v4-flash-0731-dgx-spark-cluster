#!/usr/bin/env python3
"""Recompute the frozen public inventory for a Hermes Agent checkout."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import warnings


RUNTIME_EXCLUDED_PREFIXES = (
    "tests/",
    "website/",
    "skills/",
    "optional-skills/",
    "contributors/",
    "mcp-research-data/",
)
KEY_FILES = ("AGENTS.md", "SECURITY.md", "LICENSE")
TS_TEST_PATTERN = re.compile(r"\.(?:test|spec)\.tsx?$")


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(repo), *args],
        stderr=subprocess.DEVNULL,
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def tracked_paths(repo: Path) -> list[Path]:
    raw = git(repo, "ls-files", "-z").decode("utf-8")
    return [Path(item) for item in raw.split("\0") if item]


def extension_name(path: Path) -> str:
    suffix = path.suffix.lower()
    return suffix[1:] if suffix else "[none]"


def is_python_test(path: Path) -> bool:
    value = path.as_posix()
    return value.startswith("tests/") or "/tests/" in value


def is_runtime_python(path: Path) -> bool:
    value = path.as_posix()
    return not is_python_test(path) and not value.startswith(RUNTIME_EXCLUDED_PREFIXES)


def build_snapshot(repo: Path) -> dict[str, object]:
    repo = repo.resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"not a Git checkout: {repo}")

    paths = tracked_paths(repo)
    total_bytes = 0
    text_files = 0
    text_lines = 0
    binary_files = 0
    extensions: dict[str, int] = {}
    top_levels: dict[str, int] = {}

    python_files = 0
    python_parse_errors = 0
    runtime_python_files = 0
    runtime_python_functions = 0
    runtime_python_classes = 0
    python_test_files = 0
    python_test_functions = 0
    typescript_test_files = 0

    for relative in paths:
        path = repo / relative
        payload = path.read_bytes()
        total_bytes += len(payload)
        extensions[extension_name(relative)] = extensions.get(extension_name(relative), 0) + 1
        top = relative.parts[0] if len(relative.parts) > 1 else "[root]"
        top_levels[top] = top_levels.get(top, 0) + 1

        if b"\0" in payload[:8192]:
            binary_files += 1
        else:
            text_files += 1
            text_lines += payload.count(b"\n") + int(bool(payload) and not payload.endswith(b"\n"))

        if TS_TEST_PATTERN.search(relative.as_posix()):
            typescript_test_files += 1

        if relative.suffix.lower() != ".py":
            continue
        python_files += 1
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(payload.decode("utf-8", errors="replace"))
        except (SyntaxError, ValueError):
            python_parse_errors += 1
            continue

        functions = sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for node in ast.walk(tree)
        )
        classes = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
        tests = sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name.startswith("test_")
            for node in ast.walk(tree)
        )
        if is_python_test(relative):
            python_test_files += 1
            python_test_functions += tests
        elif is_runtime_python(relative):
            runtime_python_files += 1
            runtime_python_functions += functions
            runtime_python_classes += classes

    key_hashes = {}
    for relative in KEY_FILES:
        path = repo / relative
        if not path.is_file():
            raise SystemExit(f"missing required upstream file: {relative}")
        key_hashes[relative] = sha256_bytes(path.read_bytes())

    return {
        "repository": "NousResearch/hermes-agent",
        "source_url": "https://github.com/NousResearch/hermes-agent",
        "commit": git(repo, "rev-parse", "HEAD").decode().strip(),
        "tree": git(repo, "rev-parse", "HEAD^{tree}").decode().strip(),
        "commit_time": git(repo, "log", "-1", "--format=%cI").decode().strip(),
        "inventory": {
            "tracked_files": len(paths),
            "tracked_bytes": total_bytes,
            "text_files": text_files,
            "text_lines": text_lines,
            "binary_files": binary_files,
            "extension_counts": dict(sorted(extensions.items())),
            "top_level_counts": dict(sorted(top_levels.items())),
        },
        "python_ast": {
            "python_files": python_files,
            "parse_errors": python_parse_errors,
            "runtime_python_files": runtime_python_files,
            "runtime_python_functions": runtime_python_functions,
            "runtime_python_classes": runtime_python_classes,
            "python_test_files": python_test_files,
            "python_test_functions": python_test_functions,
        },
        "typescript_tests": {
            "test_or_spec_files": typescript_test_files,
            "filename_pattern": "*.test.ts, *.test.tsx, *.spec.ts, *.spec.tsx",
        },
        "key_file_sha256": key_hashes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True, help="Hermes Agent Git checkout")
    parser.add_argument(
        "--verify",
        type=Path,
        help="Public audit-plan JSON whose source_snapshot must match",
    )
    args = parser.parse_args()

    snapshot = build_snapshot(args.repo)
    if args.verify:
        expected = json.loads(args.verify.read_text(encoding="utf-8"))["source_snapshot"]
        if snapshot != expected:
            print("HERMES SNAPSHOT VERIFY FAIL", file=sys.stderr)
            print(json.dumps({"expected": expected, "observed": snapshot}, indent=2), file=sys.stderr)
            return 1
        print("HERMES SNAPSHOT VERIFY PASS")
        print(f"commit={snapshot['commit']}")
        print(f"tracked_files={snapshot['inventory']['tracked_files']}")
        print(f"text_lines={snapshot['inventory']['text_lines']}")
        return 0

    print(json.dumps(snapshot, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
