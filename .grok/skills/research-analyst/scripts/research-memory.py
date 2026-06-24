#!/usr/bin/env python3
"""Research analyst cross-session memory."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MEMORY_DIR = "research-memory"
LOCK_TIMEOUT = 30
LOCK_POLL = 0.2
FILE_MODE = 0o600
MAX_RUNS = 30

HEADER = "# Research Analysis Memory\n\n> Maintained by /research skill.\n\n"


class MemErr(Exception):
    exit_code = 1


class LockErr(MemErr):
    exit_code = 3


class SpecErr(MemErr):
    exit_code = 4


def git(*a: str) -> str | None:
    try:
        r = subprocess.run(["git", *a], capture_output=True, text=True, timeout=5)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def workspace_id() -> str:
    remote = git("config", "--get", "remote.origin.url")
    src = remote.strip().rstrip("/").removesuffix(".git") if remote else ""
    if not src:
        cd = git("rev-parse", "--git-common-dir")
        src = str(Path(cd).resolve()) if cd else str(Path.cwd().resolve())
    h = hashlib.sha256(src.encode()).hexdigest()[:12]
    name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", src.rsplit("/", 1)[-1])[:40] or "ws"
    return f"{name}-{h}"


def paths(create: bool = False) -> dict[str, Path]:
    base = Path.home() / ".grok" / MEMORY_DIR
    if create:
        base.mkdir(parents=True, exist_ok=True)
    wid = workspace_id()
    return {"dir": base, "file": base / f"{wid}.md", "lock": base / f"{wid}.lock"}


def sanitize(t: str) -> str:
    return re.sub(r"[\r\n\t]+", " ", t).strip()


def render(run: dict[str, Any], prior: str) -> str:
    topic = sanitize(str(run.get("topic", "")))
    if not topic:
        raise SpecErr("run.topic required")
    date = run.get("date") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [HEADER, "## Latest Thread", "", f"### {topic}", f"- **Last analyzed**: {date}"]
    if run.get("effort"):
        lines.append(f"- **Effort**: {run['effort']}")
    if run.get("certainty"):
        lines.append(f"- **Certainty**: {sanitize(str(run['certainty']))}")
    for c in run.get("conclusions") or []:
        lines.append(f"- {sanitize(str(c))}")
    if run.get("open_questions"):
        lines.append("- **Open questions**:")
        for q in run["open_questions"]:
            lines.append(f"  - {sanitize(str(q))}")
    if run.get("sources"):
        lines.append(f"- **Sources**: {', '.join(sanitize(str(s)) for s in run['sources'])}")
    if run.get("guideline_flags"):
        lines.append(f"- **Guideline flags**: {sanitize(str(run['guideline_flags']))}")
    lines.extend(["", "## Recent Runs", ""])
    entry = f"### {date} — {topic}\n- Effort: {run.get('effort', '')}\n- Verdict: {sanitize(str(run.get('verdict', '')))}\n"
    old_runs = []
    if prior:
        for m in re.finditer(r"### (\d{4}-\d{2}-\d{2}) — (.+?)\n", prior):
            if m.group(2) != topic:
                old_runs.append(m.group(0))
    lines.append(entry)
    lines.extend(old_runs[: MAX_RUNS - 1])
    return "\n".join(lines).rstrip() + "\n"


def acquire(lock: Path) -> int:
    fd = os.open(str(lock), os.O_CREAT | os.O_RDWR, FILE_MODE)
    end = time.time() + LOCK_TIMEOUT
    while True:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fd
        except BlockingIOError:
            if time.time() >= end:
                os.close(fd)
                raise LockErr("lock timeout")
            time.sleep(LOCK_POLL)


def update(spec: dict[str, Any]) -> None:
    p = paths(create=True)
    prior = p["file"].read_text(encoding="utf-8") if p["file"].exists() else ""
    run = spec.get("run")
    if not isinstance(run, dict):
        raise SpecErr("run must be object")
    content = render(run, prior)
    fd = acquire(p["lock"])
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=p["dir"], delete=False) as tmp:
            tmp.write(content)
            tpath = tmp.name
        os.replace(tpath, p["file"])
        try:
            os.chmod(p["file"], FILE_MODE)
        except OSError:
            pass
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)
    print(json.dumps({"ok": True, "path": str(p["file"])}))


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("path")
    sub.add_parser("read")
    sub.add_parser("snapshot")
    sub.add_parser("update")
    args = ap.parse_args()
    try:
        p = paths()
        if args.cmd == "path":
            print(p["file"])
        elif args.cmd == "read":
            if p["file"].exists():
                print(p["file"].read_text(encoding="utf-8"), end="")
        elif args.cmd == "snapshot":
            t = p["file"].read_text(encoding="utf-8") if p["file"].exists() else ""
            print(json.dumps({"path": str(p["file"]), "content": t}))
        elif args.cmd == "update":
            update(json.load(sys.stdin))
    except MemErr as e:
        print(str(e), file=sys.stderr)
        return e.exit_code
    except json.JSONDecodeError as e:
        print(f"invalid JSON: {e}", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
