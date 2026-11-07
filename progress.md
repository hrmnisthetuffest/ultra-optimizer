# Progress log (Ultra Optimizer build)

Source of truth: `ULTRA_OPTIMIZER_CLAUDE_CODE_BUILD_SPEC.md`. Update this file after every phase.

## Environment facts (2026-11-07)
- Claude Code 2.1.319, Python 3.14.9 (no jsonschema, no PyYAML, no shellcheck, no pwsh). Validators are stdlib-only.
- Linux only. install.ps1 cannot be executed here; report as written-but-untested. macOS untested.
- Workspace root = project root (path contains a space; quote everything).
- Skills docs fetched 2026-11-07 from https://code.claude.com/docs/en/skills (frontmatter fields, 1,536-char description cap, 500-line body guidance, `$ARGUMENTS` substitution, bang-backtick injection).

## Design decisions
- `/optimize` is self-contained: no links into the race skill folder. Checklists duplicated into `optimize/checklists/`.
- SKILL.md bodies avoid the shell-injection pattern and stray dollar placeholders.
- No `allowed-tools`. `argument-hint` used (valid in Claude Code; rejected by claude.ai/API upload).
- LICENSE is a placeholder: the license choice belongs to the user.
- Hardware facts: only schema + clearly-labelled illustrative examples, plus a few records fetched from official sources with real access dates; everything else marked unverified/estimated.
- Environment note: a GateGuard hook demands stated facts before each first write of a file; facts are given in-chat, hook not disabled.

## Phase status
| Phase | Status |
|---|---|
| 1 Foundation: dirs, both SKILL.md | in progress |
| 2 Schemas + validators | pending |
| 3 Core/hardware/workload/quality refs | pending |
| 4 App/language/framework/arch/build refs | pending |
| 5 optimize refs + checklists | pending |
| 6 Installers + installer tests | pending |
| 7 Evals | pending |
| 8 Docs | pending |
| 9 Full validation + report | pending |

## Validation log
See `tests/TEST_LOG.md`.
