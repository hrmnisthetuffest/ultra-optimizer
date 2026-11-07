#!/usr/bin/env python3
"""Check that the six RACE schemas are well-formed JSON and that every example
behaves as its name says (valid-* accepted, invalid-* rejected).

Stdlib only. Run from anywhere: python3 tests/validate_schemas.py [--root DIR]
Exit code 0 = all checks pass.
"""
import argparse
import importlib.util
import json
import pathlib
import sys

EXPECTED = [
    "hardware-capability",
    "hardware-benchmark",
    "workload-profile",
    "tunable-parameter",
    "application-optimization-profile",
    "optimization-result",
]


def load_validator(root):
    path = root / ".claude" / "skills" / "race" / "scripts" / "validate_records.py"
    spec = importlib.util.spec_from_file_location("validate_records", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    root = pathlib.Path(args.root)
    vr = load_validator(root)
    sdir = root / ".claude" / "skills" / "race" / "schemas"
    failures = 0
    checks = 0

    def report(ok, msg):
        nonlocal failures, checks
        checks += 1
        if not ok:
            failures += 1
        print(("PASS " if ok else "FAIL ") + msg)

    for name in EXPECTED:
        sp = sdir / (name + ".schema.json")
        try:
            schema = json.loads(sp.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            report(False, "%s schema loads (%s)" % (name, e))
            continue
        report(True, "%s schema loads" % name)
        report(bool(schema.get("schema_version")), "%s has schema_version" % name)
        for kind in ("valid", "invalid"):
            ep = sdir / "examples" / ("%s-%s.json" % (kind, name))
            if not ep.exists():
                report(False, "%s example exists: %s" % (kind, ep.name))
                continue
            rec = json.loads(ep.read_text(encoding="utf-8"))
            errs = vr.validate(rec, schema)
            if kind == "valid":
                report(not errs, "%s accepted %s" % (ep.name, errs[:2] if errs else ""))
            else:
                report(bool(errs), "%s rejected (%d errors)" % (ep.name, len(errs)))

    print("\n%d checks, %d failures" % (checks, failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
