# Contributing

- Keep `SKILL.md` files under 500 lines; put detail in references.
- Reference files use the 13-section format and must state sources, access dates and confidence. Never fabricate hardware or benchmark data; mark unfetched claims `unverified`.
- `/optimize` must not link to or invoke `/race` files. Keep the two skills self-contained.
- Do not add `allowed-tools` to either skill.
- Before sending changes run every command in `docs/BUILD_AND_RELEASE.md`.
- Write installer tests against scratch directories only; never touch a real `~/.claude/skills`.
