# /server-optimize

## What it does
Coordinates server and backend optimization. It first collects every material setting in one intake, then applies three lenses without duplicating knowledge: universal code improvements (as `/optimize` would), hardware-aware strategy selection from verified facts (as `/race` would), and network attribution (as `/ping-optimize` would). It never invokes the sibling skills; it applies their guidance itself, and each sibling can use the shared library through its own `references/server-integration.md`.

## Intake
Run `python3 .claude/skills/server-optimize/scripts/detect_deployment.py PROJECT_ROOT --intake`. The output holds the ten intake items with prefilled, detected values marked `detected-from-repository`. Every item accepts `unknown` or `not-applicable`. Never paste secrets; credentials come from your existing secret mechanism.

## Access levels
repo-only (default) -> read-only inspection -> read-only metrics -> staging profiling -> authorized staging changes -> authorized production changes. Restarts, migrations, scaling, firewall changes and deploys always need explicit authorization for that environment.

## Custom deployment profile
Describe your deployment with `schemas/deployment-profile.schema.json`; see `schemas/examples/valid-custom-profile.json`. Each fact records its source (detected, developer-provided, verified-live, unknown). Unverified facts are never treated as verified.

## Runtime adaptation
Approve a policy with `schemas/server-adaptation-policy.schema.json`. The reference model in `templates/server_adaptation_model.py` derives worker counts, cache budgets and pool sizes from verified capabilities, clamps them to your approved ranges, and restores the last known-good values when validation fails. It is an executable contract, not drop-in production code, and it never touches OS or infrastructure settings.

## Limitations
Detection rules are heuristic and unverified against provider changes. Domain references cite no external sources yet; verify platform limits against current official documentation. No live infrastructure was available, so live inspection, staging profiling and production rollback were not exercised.
