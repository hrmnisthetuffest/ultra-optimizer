# Build and release

No build step. Validate and test:

```
python3 -I tests/validate_skill_structure.py --strict-refs
python3 -I tests/validate_schemas.py
python3 -I tests/test_race_reference_model.py
python3 -I tests/test_fixtures.py
python3 -I tests/test_installers.py
```

Release checklist: all of the above pass; `CHANGELOG.md` updated; LICENSE chosen by the owner (a placeholder ships); Windows installers tested on Windows; live `/race` and `/optimize` resolution checked in Claude Code; evals run in fresh sessions (see `tests/TEST_LOG.md` for status).
Note: `argument-hint` is valid in Claude Code but would be rejected by claude.ai or Skills-API uploads; remove it for those targets.
