# Privacy and safety

- Local by default. No telemetry by default. No serial numbers, accounts, content, passwords or tokens in profiles.
- External telemetry requires explicit developer decision, user consent, disclosure, retention controls and secure transport (`references/core/privacy-and-consent.md`).
- Coarse capability classes are stored instead of raw identifiers.
- Zero known functional regressions is the enforceable standard: preserve documented and observed behavior, run relevant tests, disclose untested areas, roll back failed changes. Equivalence is never claimed as proven.
- No destructive or external actions (reset, clean, force-push, publish, deploy, PR) without authorization.
- Installers touch only their own directories, back up before replacing, and uninstall only unmodified owned files.
