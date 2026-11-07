# server-optimize evals

`evals.json` uses the skill-creator format. Cases marked `should_trigger: false` are requests where the skill
must refuse the unsafe part (production restarts or migrations without authorization, secrets in chat,
unauthorized scaling, OS/BIOS/firmware changes, AI features). Fixture paths are relative to the repository root.

Static checks run in `tests/test_server_optimize.py` and `tests/validate_skill_structure.py`. The prompts were
NOT executed against a live model in this build; run them manually or with skill-creator.
