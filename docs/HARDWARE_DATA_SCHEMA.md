# Hardware data schemas

Six JSON Schemas live in `.claude/skills/race/schemas/`: `hardware-capability`, `hardware-benchmark`, `workload-profile`, `tunable-parameter`, `application-optimization-profile`, `optimization-result`.

- Unknowns are explicit: `"unknown"` or `"unsupported"`, never guessed.
- Evidence confidence labels: `official-specification`, `independently-measured`, `internally-measured`, `estimated`, `unknown`, `unverified`.
- Benchmark records require tool/version, software and driver versions, source and date.
- `schemas/examples/` holds **illustrative** valid/invalid records; they are not real measurements.
- Curated records: only NVIDIA compute capabilities for four GPUs (source URL and access date in `references/hardware/nvidia-gpu-architectures.md`). No exhaustive SKU database is shipped.
- Validate with `python3 -I .claude/skills/race/scripts/validate_records.py SCHEMA RECORD...` (stdlib subset validator; uses `jsonschema` if installed).
