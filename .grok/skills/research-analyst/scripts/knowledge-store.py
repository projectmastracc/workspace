#!/usr/bin/env python3
"""Lightweight helpers for repo-local knowledge/ compound and interaction profiles."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


def repo_root() -> Path:
    # scripts/ → research-analyst/ → skills/ → .grok/ → repo
    return Path(__file__).resolve().parents[4]


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "unknown"


def compound_dir(slug: str) -> Path:
    return repo_root() / "knowledge" / "compounds" / slug


def interaction_dir(slug_a: str, slug_b: str) -> Path:
    a, b = slugify(slug_a), slugify(slug_b)
    return repo_root() / "knowledge" / "interactions" / f"{a}_vs_{b}"


def cmd_slug(args: argparse.Namespace) -> int:
    print(slugify(args.name))
    return 0


def cmd_path(args: argparse.Namespace) -> int:
    if args.kind == "compound":
        print(compound_dir(slugify(args.name)))
    else:
        print(interaction_dir(args.name_a, args.name_b))
    return 0


def cmd_read(args: argparse.Namespace) -> int:
    if args.kind == "compound":
        d = compound_dir(slugify(args.name))
    else:
        d = interaction_dir(args.name_a, args.name_b)
    profile = d / "profile.md"
    meta = d / "meta.json"
    if not profile.exists():
        print("none")
        return 0
    print(f"# Prior knowledge: {d}")
    print()
    print(profile.read_text(encoding="utf-8"))
    if meta.exists():
        print("\n---\n## meta.json\n")
        print(meta.read_text(encoding="utf-8"))
    return 0


def cmd_write(args: argparse.Namespace) -> int:
    if args.kind == "compound":
        d = compound_dir(slugify(args.name))
        slug = slugify(args.name)
    else:
        d = interaction_dir(args.name_a, args.name_b)
        slug = f"{slugify(args.name_a)}_vs_{slugify(args.name_b)}"

    d.mkdir(parents=True, exist_ok=True)

    profile_src = Path(args.profile)
    matrix_src = Path(args.matrix) if args.matrix else None

    (d / "profile.md").write_text(profile_src.read_text(encoding="utf-8"), encoding="utf-8")
    if matrix_src and matrix_src.exists():
        (d / "matrix.json").write_text(matrix_src.read_text(encoding="utf-8"), encoding="utf-8")

    meta = {
        "slug": slug,
        "updated": args.date or date.today().isoformat(),
        "effort": args.effort,
        "overall_certainty": args.certainty,
        "input_type": "interaction" if args.kind == "interaction" else "compound",
        "open_questions": args.open_question or [],
    }
    if args.lenses:
        meta["lenses"] = args.lenses
    (d / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(str(d))
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("slug", help="Normalize a compound name to a slug")
    s.add_argument("name")
    s.set_defaults(func=cmd_slug)

    s = sub.add_parser("path", help="Print knowledge directory path")
    s.add_argument("kind", choices=["compound", "interaction"])
    s.add_argument("name", nargs="?", help="Compound name (compound kind)")
    s.add_argument("name_a", nargs="?", help="Compound A (interaction)")
    s.add_argument("name_b", nargs="?", help="Compound B (interaction)")
    s.set_defaults(func=cmd_path)

    s = sub.add_parser("read", help="Print prior profile or 'none'")
    s.add_argument("kind", choices=["compound", "interaction"])
    s.add_argument("name", nargs="?", help="Compound name")
    s.add_argument("name_a", nargs="?", help="Compound A")
    s.add_argument("name_b", nargs="?", help="Compound B")
    s.set_defaults(func=cmd_read)

    s = sub.add_parser("write", help="Write profile + meta (+ optional matrix)")
    s.add_argument("kind", choices=["compound", "interaction"])
    s.add_argument("--name", help="Compound name")
    s.add_argument("--name-a", dest="name_a")
    s.add_argument("--name-b", dest="name_b")
    s.add_argument("--profile", required=True, help="Path to briefing/profile.md")
    s.add_argument("--matrix", help="Path to evidence-matrix.json")
    s.add_argument("--effort", type=int, default=3)
    s.add_argument("--certainty", default="Unknown")
    s.add_argument("--date")
    s.add_argument("--open-question", action="append")
    s.add_argument("--lenses", nargs="*")
    s.set_defaults(func=cmd_write)

    args = p.parse_args()
    if args.cmd == "path" and args.kind == "compound" and not args.name:
        print("name required for compound", file=sys.stderr)
        return 2
    if args.cmd in ("path", "read") and args.kind == "interaction" and not (args.name_a and args.name_b):
        # allow: path interaction name_a name_b via positional reuse
        if args.name and args.name_a and not args.name_b:
            args.name_b = args.name_a
            args.name_a = args.name
        elif args.name and not args.name_a:
            print("name_a and name_b required for interaction", file=sys.stderr)
            return 2
    if args.cmd == "write":
        if args.kind == "compound" and not args.name:
            print("--name required for compound", file=sys.stderr)
            return 2
        if args.kind == "interaction" and not (args.name_a and args.name_b):
            print("--name-a and --name-b required for interaction", file=sys.stderr)
            return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
