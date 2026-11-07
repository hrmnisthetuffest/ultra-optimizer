# RACE evaluations

`evals.json` follows the skill-creator format (`skill_name`, `evals[]` with `prompt`, `expected_output`) plus a `should_trigger` flag for routing cases. Statuses are recorded in `tests/TEST_LOG.md`. These cases were authored but **not yet run in fresh Claude Code sessions** unless the log says so. Classification fixtures live in `tests/fixtures/` and are tested deterministically by `tests/test_fixtures.py`.
