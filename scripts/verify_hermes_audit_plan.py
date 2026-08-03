#!/usr/bin/env python3
"""Verify the frozen pre-run Hermes audit contract and documentation anchors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "data" / "hermes-audit-plan.json"
DOCS = (
    ROOT / "docs" / "HERMES-AUDIT-PLAN.md",
    ROOT / "docs" / "HERMES-AUDIT-VERIFICATION-CONTRACT.md",
    ROOT / "docs" / "HERMES-AUDIT-DISCLOSURE.md",
)
SHA40 = re.compile(r"^[0-9a-f]{40}$")
SHA64 = re.compile(r"^[0-9a-f]{64}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    payload = json.loads(PLAN.read_text(encoding="utf-8"))
    require(payload["schema_version"] == 1, "unexpected schema version")
    require(payload["record_status"] == "planned_not_run", "record must remain pre-run")
    require(payload["results_status"] == "no_results_collected", "results must be absent")

    snapshot = payload["source_snapshot"]
    require(SHA40.fullmatch(snapshot["commit"]) is not None, "invalid source commit")
    require(SHA40.fullmatch(snapshot["tree"]) is not None, "invalid source tree")
    require(snapshot["repository"] == "NousResearch/hermes-agent", "wrong upstream repository")
    require(snapshot["python_ast"]["parse_errors"] == 0, "snapshot contains Python parse errors")
    require(
        snapshot["inventory"]["text_files"] + snapshot["inventory"]["binary_files"]
        == snapshot["inventory"]["tracked_files"],
        "text/binary count does not cover tracked files",
    )
    for name, digest in snapshot["key_file_sha256"].items():
        require(SHA64.fullmatch(digest) is not None, f"invalid key-file hash: {name}")

    contract = payload["audit_contract"]
    lanes = contract["workflow_allocation"]
    require(sum(item["workflows"] for item in lanes) == 1024, "workflow lanes do not total 1,024")
    require(contract["total_workflows"] == 1024, "unexpected workflow total")
    require(contract["real_audit_units"] == 960, "unexpected real-unit total")
    require(contract["positive_controls"] == 32, "unexpected positive-control total")
    require(contract["negative_controls"] == 32, "unexpected negative-control total")
    require(len(contract["model_stages"]) == 3, "audit workflow must have three model stages")
    require(contract["model_calls_expected"] == 3072, "expected model-call count is inconsistent")

    commit = snapshot["commit"]
    for path in DOCS:
        text = path.read_text(encoding="utf-8")
        require(commit in text, f"source commit missing from {path.name}")
        require("planned" in text.lower(), f"pre-run label missing from {path.name}")

    print("HERMES AUDIT PLAN VERIFY PASS")
    print(f"record_sha256={sha256(PLAN)}")
    print(f"source_commit={commit}")
    print(f"workflow_total={contract['total_workflows']}")
    print(f"model_calls_expected={contract['model_calls_expected']}")
    print("results_status=no_results_collected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
