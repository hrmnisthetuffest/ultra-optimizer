#!/usr/bin/env python3
"""Validate RACE JSON records against RACE schemas (stdlib only).

Uses `jsonschema` when installed, otherwise a built-in subset validator that
supports: type, enum, const, required, properties, additionalProperties,
items, minItems/maxItems, minLength, minimum/maximum, pattern, anyOf, oneOf,
and local "$ref" of the form "#/$defs/name".

Usage: validate_records.py SCHEMA.json RECORD.json [RECORD.json ...]
Exit code 0 = all valid, 1 = invalid, 2 = usage/IO error.
"""
import json
import re
import sys

TYPES = {
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "array": lambda v: isinstance(v, list),
    "object": lambda v: isinstance(v, dict),
    "null": lambda v: v is None,
}


def _resolve(root, ref):
    if not ref.startswith("#/"):
        raise ValueError("only local refs supported: %s" % ref)
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def check(value, schema, root, path="$"):
    """Return list of error strings (empty = valid)."""
    errors = []
    if "$ref" in schema:
        errors += check(value, _resolve(root, schema["$ref"]), root, path)
        rest = {k: v for k, v in schema.items() if k not in ("$ref", "description")}
        if not rest:
            return errors
        schema = rest
    if "const" in schema and value != schema["const"]:
        errors.append("%s: must equal %r" % (path, schema["const"]))
    if "enum" in schema and value not in schema["enum"]:
        errors.append("%s: %r not in enum %r" % (path, value, schema["enum"]))
    t = schema.get("type")
    if t is not None:
        ts = t if isinstance(t, list) else [t]
        if not any(TYPES[x](value) for x in ts):
            errors.append("%s: expected type %s, got %s" % (path, "/".join(ts), type(value).__name__))
            return errors
    if "anyOf" in schema:
        if not any(not check(value, s, root, path) for s in schema["anyOf"]):
            errors.append("%s: matches none of anyOf" % path)
    if "oneOf" in schema:
        n = sum(1 for s in schema["oneOf"] if not check(value, s, root, path))
        if n != 1:
            errors.append("%s: matches %d of oneOf (need exactly 1)" % (path, n))
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append("%s: shorter than minLength %d" % (path, schema["minLength"]))
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append("%s: %r does not match pattern %s" % (path, value, schema["pattern"]))
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append("%s: %r below minimum %r" % (path, value, schema["minimum"]))
        if "maximum" in schema and value > schema["maximum"]:
            errors.append("%s: %r above maximum %r" % (path, value, schema["maximum"]))
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append("%s: fewer than %d items" % (path, schema["minItems"]))
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append("%s: more than %d items" % (path, schema["maxItems"]))
        if "items" in schema:
            for i, item in enumerate(value):
                errors += check(item, schema["items"], root, "%s[%d]" % (path, i))
    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                errors.append("%s: missing required property %r" % (path, req))
        props = schema.get("properties", {})
        for k, v in value.items():
            if k in props:
                errors += check(v, props[k], root, "%s.%s" % (path, k))
            else:
                ap = schema.get("additionalProperties", True)
                if ap is False:
                    errors.append("%s: unexpected property %r" % (path, k))
                elif isinstance(ap, dict):
                    errors += check(v, ap, root, "%s.%s" % (path, k))
    return errors


def validate(record, schema):
    """Validate one record; returns list of errors."""
    try:  # prefer the real library if present
        import jsonschema  # type: ignore
        validator = jsonschema.Draft202012Validator(schema)
        return ["%s: %s" % ("$" + "".join("[%r]" % p for p in e.absolute_path), e.message)
                for e in validator.iter_errors(record)]
    except ImportError:
        return check(record, schema, schema)


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    try:
        with open(argv[1], encoding="utf-8") as f:
            schema = json.load(f)
    except (OSError, ValueError) as e:
        print("cannot load schema: %s" % e)
        return 2
    bad = 0
    for rec_path in argv[2:]:
        try:
            with open(rec_path, encoding="utf-8") as f:
                record = json.load(f)
        except (OSError, ValueError) as e:
            print("FAIL %s: cannot load: %s" % (rec_path, e))
            bad += 1
            continue
        errs = validate(record, schema)
        if errs:
            bad += 1
            print("FAIL %s" % rec_path)
            for e in errs:
                print("  - " + e)
        else:
            print("OK   %s" % rec_path)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
