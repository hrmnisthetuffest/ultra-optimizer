# optimize evaluations

`evals.json` uses the skill-creator format with a `should_trigger` flag. `/optimize` has `disable-model-invocation: true`, so the last case checks that it is never auto-selected. Execution status is tracked in `tests/TEST_LOG.md`.
