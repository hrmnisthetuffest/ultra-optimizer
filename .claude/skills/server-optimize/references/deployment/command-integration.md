<!-- format: 13-section -->
# Sharing server intelligence across the four commands

## 1. Purpose and applicability
Explain how /race, /optimize, /ping-optimize and /server-optimize use one shared library without duplicating it or blurring responsibilities.

## 2. Detection signals
A command encounters backend or server code, deployment files or a request about server performance.

## 3. What to inspect
Which lens applies: hardware-aware (/race), universal (/optimize), network-aware (/ping-optimize) or orchestrating (/server-optimize). Shared material lives in this skill's references (server-domains, deployment), schemas and detection script. The other three skills each carry a short server-integration reference that names the shared files and states their own boundary; they do not copy the domain content.

## 4. Metrics
Shared files referenced versus duplicated (target: none duplicated), boundary violations found in review.

## 5. Common bottlenecks and anti-patterns
Copying domain references into other skills, letting /optimize use hardware or network specifics, letting /race rewrite universal code without measurement, letting any command invoke another automatically, introducing AI services.

## 6. Candidate optimization techniques
Each command loads only the shared domain files relevant to the component in front of it. When server-optimize is not installed, the other commands continue with their own references and state that the shared library is unavailable. /server-optimize applies the three lenses itself, in order: universal, then hardware-aware, then network-aware, and may recommend running the sibling commands but does not invoke them.

## 7. Runtime tunables versus build-time changes
Runtime: none.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: hardware-aware selection from verified server capabilities. /optimize lens: device-independent code and design improvements only. /ping-optimize lens: latency, endpoint response, connection behavior, bandwidth, loss.

## 9. Compatibility and version considerations
Installers install each skill independently; cross-skill links are plain-text names, never relative paths, so single-skill installs stay valid.

## 10. Security, privacy and accessibility considerations
A shared library must not become a way for one command to widen another's authority; access levels and authorizations apply per command invocation. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
tests/validate_skill_structure.py checks that other skills reference the shared library by name only, that each integration reference has the 13 sections, and that no skill links into another skill's directory.

## 12. Rollback and failure handling
Removing server-optimize must leave the other three skills valid and working. Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
