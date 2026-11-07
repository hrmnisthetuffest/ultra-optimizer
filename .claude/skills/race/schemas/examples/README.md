# Schema examples (illustrative only)

Every file in this directory is **illustrative**. The values are invented to show the shape of each record. They are **not** real measurements, real hardware specifications, or knowledge-base evidence, and must never be copied into a knowledge base as facts.

- `valid-*.json` must validate against the matching schema.
- `invalid-*.json` must be rejected; they exist to prove the schemas actually reject bad records (out-of-range values, unknown fields, guessed values).

Validate with `python3 tests/validate_schemas.py` from the repository root.
