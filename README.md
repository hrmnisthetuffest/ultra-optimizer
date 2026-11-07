<div align="center">

# Ultra Optimizer

**Four Claude Code skills that make your app faster without touching your machine, your network or your security.**

![license](https://img.shields.io/badge/license-MIT-blue)
![claude code](https://img.shields.io/badge/Claude%20Code-skills-8A63D2)
![tests](https://img.shields.io/badge/tests-local%20suite%20passing-brightgreen)
![status](https://img.shields.io/badge/status-early-orange)

</div>

## Why this exists

Software today often runs the same way on a ten-year-old laptop and a workstation with 64 cores. Many apps ship with settings picked for the developer's machine, then feel sluggish, hog memory or ignore the hardware sitting idle on yours. Most of us have used something that was clearly never tuned for the computer in front of us.

The idea behind RACE is that an app can look at the machine it is actually running on, and at how you actually use it, and tune its own behavior to fit: more parallel work where there are spare cores, smaller caches where memory is tight, backing off while you are busy. The app adapts to you instead of asking you to dig through settings or buy new hardware.

That only works if it is done carefully, which is why every command here is bounded, measured and reversible. This is an early project by a 15-year-old developer, so the foundations are tested, but real-world benchmarks are still to come, and feedback is welcome.

## What it is

Ultra Optimizer is a set of slash commands for [Claude Code](https://claude.com/claude-code). Each one has a strict job and a strict boundary, so you always know what it will and will not change.

| Command | Job | Hard boundary |
|---|---|---|
| `/race` | Hardware-aware optimization: adapts the app's own behavior to detected CPU, memory and real workloads. | Never edits BIOS, firmware, drivers or OS settings. |
| `/optimize` | Universal, device-independent code and architecture improvements. | Never looks at your hardware or network. Runs only when you call it. |
| `/ping-optimize` | Network latency and transfer efficiency in the app's own networking code. | Never touches router, DNS, VPN or OS settings. |
| `/server-optimize` | Backend and deployment analysis with one upfront intake. | Repo-only by default; live or production changes need explicit approval. |

## RACE in depth

RACE (Runtime Adaptive Configuration Engine) is the core of the suite. Most "optimize for this machine" code hard-codes guesses. RACE instead gives an application a small, auditable layer that reads what the machine really has and how the app is really being used, then adjusts only the app's own settings.

**What it does**

- **Detects** CPU, memory and workload shape at runtime, and records which facts were verified and which are only estimated.
- **Adapts bounded settings**: worker counts, concurrency, cache sizes, batch sizes and scheduling. Each setting has a developer-approved range, and a value outside that range is rejected.
- **Stays polite**: adaptation work pauses while the user is active and only counts cumulative foreground time toward its thresholds.
- **Rolls back**: every change is validated against a baseline, and the last known-good configuration is restored if validation fails.
- **Stays honest**: no speedup is claimed without a before/after measurement.

**What it never does:** edit BIOS, firmware, drivers, OS power settings or graphics settings, and it adds no AI features unless you ask for them.

**Subcommands:** `/race build`, `audit`, `benchmark`, `status`, `improve`, `integrate` and `review`. Build creates the layer in a project, audit checks an existing one, and integrate wires it into code you already have.

The repo includes a small stdlib Python reference model of the registry, scheduler and rollback logic (`.claude/skills/race/templates/`), with tests for the cumulative-foreground threshold, pause-on-activity, out-of-range rejection and last-known-good restore. It is an executable contract for the behavior, not universal runtime code. It has not been measured on real hardware fleets.

## Principles

- **Measure first.** No claimed speedup without a baseline and a before/after.
- **Preserve behavior.** Features, APIs, auth and data integrity come before speed.
- **Roll back on failure.** If validation fails, the last known-good state is restored.
- **No surprise AI.** AI features are never added unless you choose them.
- **No guessing.** Hardware and server facts are marked detected, developer-provided, verified or unknown.

## Install
Requires bash, `cp`, `find`, `sha256sum` or `shasum`. Run from the project you want to add the skills to:

```
bash /path/to/ultra-optimizer/install/install.sh --scope project      # ./.claude/skills
bash /path/to/ultra-optimizer/install/install.sh --scope personal     # ~/.claude/skills
```
Flags: `--target DIR`, `--only race|optimize|ping-optimize|server-optimize`, `--yes`, `--dry-run`, `--force-backup`. Existing `race`/`optimize` folders are never replaced without confirmation and a timestamped backup. Unrelated skills are never touched. Note: personal skills take precedence over project skills of the same name.

Uninstall: `bash install/uninstall.sh --scope project` (removes only unmodified files recorded in the manifest).
Windows: `install/install.ps1` and `uninstall.ps1` are written but **untested**.
Manual fallback: copy `.claude/skills/race` and `.claude/skills/optimize` into your skills directory.

## Use
```
/race build | audit | benchmark | status | improve | integrate | review
/optimize audit | apply | review | report
/server-optimize [scope, e.g. 'docker app slow under load', 'database queries']
/ping-optimize [scope, e.g. 'browser navigation', 'API response times', 'download performance']
```
Restart or reopen Claude Code after install and confirm the commands appear in `/`. Name collisions with existing skills are reported, not overwritten.

## Verify
See `docs/BUILD_AND_RELEASE.md`. Current results are in `tests/TEST_LOG.md`; progress in `progress.md`.

## Layout
`.claude/skills/race/` (SKILL.md, references, schemas, templates, scripts, evals) · `.claude/skills/optimize/` (SKILL.md, references, checklists, evals) · `.claude/skills/ping-optimize/` (SKILL.md, 38 references, simulator + reference retry/concurrency model, stack detector, evals) · `.claude/skills/server-optimize/` (SKILL.md, 26 domain + 7 deployment references, schemas, detector, adaptation model, evals) · `docs/` · `install/` · `tests/`.

## License
MIT. See [LICENSE](LICENSE).

## Built with
The skills, references and tests in this repo were written with the help of Claude Code and then checked by the local test suite. Evals have not been run against a live model yet, and the PowerShell installers are untested. See `tests/TEST_LOG.md` for exactly what has and has not been verified.

