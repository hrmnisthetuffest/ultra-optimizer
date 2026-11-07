# ping-optimize evals

`evals.json` uses the skill-creator format. `should_trigger: false` cases are requests where the skill must
either not be selected or must refuse the unsafe part (device network settings, disabled TLS verification,
blind retry of non-idempotent calls, unauthorized load tests, AI features, work that belongs to /race or /optimize).

Static checks (run by `tests/test_ping_optimize_model.py` and `tests/validate_skill_structure.py`) verify
structure and references. The prompts themselves were NOT executed against a live model in this build;
run them manually or with skill-creator.
