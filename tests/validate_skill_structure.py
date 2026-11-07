#!/usr/bin/env python3
"""Structural validator for the Ultra Optimizer skill suite (stdlib only).

Checks both skills: frontmatter on line 1, name == directory, description
length, SKILL.md < 500 lines, relative links resolve, invocation flags,
no allowed-tools, no shell-injection pattern, reference files carry the
13 standard headings, and /optimize never references race paths.

Usage: python3 tests/validate_skill_structure.py [--root DIR] [--strict-refs]
Exit code 0 = all checks pass.
"""
import argparse
import re
import sys
from pathlib import Path

DESC_MAX = 1536
BODY_MAX_LINES = 500
SECTION_KEYWORDS = [  # 13 standard sections (spec section 14), matched loosely by heading text
    "purpose", "detection", "inspect", "metrics", "bottleneck", "technique",
    "tunable", "hardware-dependent", "compatib", "security", "validation",
    "rollback", "sources",
]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
INJECT_RE = re.compile(r"(^|\s)!`")
FENCE_BANG_RE = re.compile(r"^```!", re.M)


def parse_frontmatter(text):
    """Minimal YAML subset: top-level `key: value` pairs. Returns (dict, body) or (None, text)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    fm = {}
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return fm, "\n".join(lines[i + 1:])
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", lines[i])
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return None, text


class Report:
    def __init__(self):
        self.fail = []
        self.ok = 0

    def check(self, cond, msg):
        if cond:
            self.ok += 1
        else:
            self.fail.append(msg)


def links_in(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore fenced code
    text = re.sub(r"`[^`]*`", "", text)
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        yield target.split("#")[0]


def check_links(rep, path):
    for t in links_in(path):
        if not t:
            continue
        rep.check((path.parent / t).exists(), f"{path}: broken link -> {t}")


def check_skill(rep, root, name, expect_disable):
    sdir = root / ".claude" / "skills" / name
    skill = sdir / "SKILL.md"
    rep.check(skill.is_file(), f"{name}: SKILL.md missing")
    if not skill.is_file():
        return
    text = skill.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    rep.check(fm is not None, f"{name}: frontmatter must start on line 1 and be closed")
    if fm is None:
        return
    rep.check(fm.get("name") == name, f"{name}: name '{fm.get('name')}' != directory")
    d = fm.get("description", "")
    rep.check(0 < len(d) <= DESC_MAX, f"{name}: description length {len(d)} not in 1..{DESC_MAX}")
    rep.check("allowed-tools" not in fm, f"{name}: allowed-tools must not be set")
    has_dmi = fm.get("disable-model-invocation", "").lower() == "true"
    rep.check(has_dmi == expect_disable, f"{name}: disable-model-invocation expected {expect_disable}")
    rep.check("argument-hint" in fm, f"{name}: argument-hint missing")
    rep.check(len(text.split("\n")) < BODY_MAX_LINES, f"{name}: SKILL.md >= {BODY_MAX_LINES} lines")
    rep.check(not INJECT_RE.search(body) and not FENCE_BANG_RE.search(body),
              f"{name}: shell-injection pattern present in SKILL.md body")
    # only $ARGUMENTS allowed as dollar substitution
    stray = [m for m in re.findall(r"\$[A-Za-z0-9_\[{]+", body) if not m.startswith("$ARGUMENTS")]
    rep.check(not stray, f"{name}: stray dollar substitution tokens {stray}")
    check_links(rep, skill)


def check_references(rep, root, strict):
    refdir = root / ".claude" / "skills" / "race" / "references"
    if not refdir.is_dir():
        rep.check(False, "race/references missing")
        return
    for f in sorted(refdir.rglob("*.md")):
        if f.name.upper() == "INDEX.MD" or f.name.startswith("_"):
            continue
        text = f.read_text(encoding="utf-8")
        if "roadmap-only" in text[:400]:
            continue
        heads = " ".join(h.lower() for h in re.findall(r"^#{2,3}\s+(.*)$", text, re.M))
        missing = [k for k in SECTION_KEYWORDS if k not in heads]
        if strict or "format: 13-section" in text[:600]:
            rep.check(not missing, f"{f.relative_to(root)}: missing standard sections {missing}")
        check_links(rep, f)


def check_optimize_isolation(rep, root):
    odir = root / ".claude" / "skills" / "optimize"
    pat = re.compile(r"\.\./race|skills/race/|references/(core|hardware)/", re.I)
    for f in sorted(odir.rglob("*")):
        if f.is_file() and f.suffix in {".md", ".json"}:
            text = f.read_text(encoding="utf-8")
            rep.check(not pat.search(text), f"{f.relative_to(root)}: references race paths")
            if f.suffix == ".md":
                check_links(rep, f)


def check_race_isolation(rep, root):
    # /race must not delegate to /optimize paths
    rdir = root / ".claude" / "skills" / "race"
    pat = re.compile(r"\.\./optimize|skills/optimize/", re.I)
    for f in sorted(rdir.rglob("*.md")):
        rep.check(not pat.search(f.read_text(encoding="utf-8")), f"{f.relative_to(root)}: references optimize paths")


def check_index(rep, root):
    idx = root / ".claude" / "skills" / "race" / "references" / "INDEX.md"
    rep.check(idx.is_file(), "race/references/INDEX.md missing")
    if idx.is_file():
        check_links(rep, idx)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--strict-refs", action="store_true", help="require 13 sections in every reference")
    a = ap.parse_args()
    root = Path(a.root)
    rep = Report()
    check_skill(rep, root, "race", expect_disable=False)
    check_skill(rep, root, "optimize", expect_disable=True)
    check_references(rep, root, a.strict_refs)
    check_optimize_isolation(rep, root)
    check_race_isolation(rep, root)
    check_index(rep, root)
    print(f"checks passed: {rep.ok}; failed: {len(rep.fail)}")
    for m in rep.fail:
        print("FAIL:", m)
    return 1 if rep.fail else 0


if __name__ == "__main__":
    sys.exit(main())
