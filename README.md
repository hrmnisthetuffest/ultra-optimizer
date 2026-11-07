# Ultra Optimizer

A Claude Code skill suite with two separate commands:

- **`/race`**: builds, integrates, audits and improves RACE (Runtime Adaptive Configuration Engine), hardware-aware optimization that adapts an application's *own* behavior to detected hardware and real workloads. Claude may auto-select it for clear hardware-aware performance requests.
- **`/ping-optimize`**: network-latency and transfer-efficiency optimization of the application's own networking code (never device, router, DNS, VPN or OS settings). Can use measured network conditions for application-level adaptation; independent of `/race` and `/optimize`; no AI features unless selected.
- **`/optimize`**: universal, device-independent code and engineering optimization. Runs only when you invoke it. Never detects hardware and never calls `/race`.

AI features are never added unless you explicitly select them. RACE never modifies BIOS, firmware, drivers, OS power or graphics settings.

## Install
Requires bash, `cp`, `find`, `sha256sum` or `shasum`. Run from the project you want to add the skills to:

```
bash /path/to/ultra-optimizer/install/install.sh --scope project      # ./.claude/skills
bash /path/to/ultra-optimizer/install/install.sh --scope personal     # ~/.claude/skills
```
Flags: `--target DIR`, `--only race|optimize|ping-optimize`, `--yes`, `--dry-run`, `--force-backup`. Existing `race`/`optimize` folders are never replaced without confirmation and a timestamped backup. Unrelated skills are never touched. Note: personal skills take precedence over project skills of the same name.

Uninstall: `bash install/uninstall.sh --scope project` (removes only unmodified files recorded in the manifest).
Windows: `install/install.ps1` and `uninstall.ps1` are written but **untested**.
Manual fallback: copy `.claude/skills/race` and `.claude/skills/optimize` into your skills directory.

## Use
```
/race build | audit | benchmark | status | improve | integrate | review
/optimize audit | apply | review | report
/ping-optimize [scope, e.g. 'browser navigation', 'API response times', 'download performance']
```
Restart or reopen Claude Code after install and confirm both commands appear in `/`. Name collisions with existing skills are reported, not overwritten.

## Verify
See `docs/BUILD_AND_RELEASE.md`. Current results are in `tests/TEST_LOG.md`; progress in `progress.md`.

## Layout
`.claude/skills/race/` (SKILL.md, references, schemas, templates, scripts, evals) · `.claude/skills/optimize/` (SKILL.md, references, checklists, evals) · `.claude/skills/ping-optimize/` (SKILL.md, 38 references, simulator + reference retry/concurrency model, stack detector, evals) · `docs/` · `install/` · `tests/`.

## License
Not yet chosen. See `LICENSE`.
