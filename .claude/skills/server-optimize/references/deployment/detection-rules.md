<!-- format: 13-section -->
# Deployment detection rules

## 1. Purpose and applicability
Explain how deployment targets are inferred from repository files and how to extend the rules. Detection supplies prefilled intake answers; it never proves what runs in production.

## 2. Detection signals
Provider config files (for example vercel.json, wrangler.toml, fly.toml, render.yaml, firebase.json), container files (Dockerfile, Compose), Kubernetes manifests and Helm/Kustomize files, IaC provider blocks, process-manager and web-server configs.

## 3. What to inspect
Run scripts/detect_deployment.py PROJECT_ROOT [--intake]. Rules live in scripts/detection-rules.json. Only file and directory names are used for environment hints; contents of .env files, keys, credentials, tfstate and kubeconfig are never opened. Supported by default: AWS, Google Cloud, Azure, Vercel, Cloudflare, Railway, Render, Fly.io, Supabase, Firebase, Docker, Kubernetes, VPS/self-hosted (unconfirmed). Dedicated servers cannot be distinguished from VPS by repository files, so they come only from the intake or custom profile.

## 4. Metrics
Per target: confidence (high or medium), evidence list (file and signal). Every result carries status detected-from-repository and verified_live false.

## 5. Common bottlenecks and anti-patterns
Treating a client dependency (for example a Supabase client library) as proof of hosting; inferring region, instance size or plan from file names; opening secret-bearing files to look for hints; assuming one detected target means a single environment.

## 6. Candidate optimization techniques
Add a target by appending an object to scripts/detection-rules.json (id, category, files, globs, content patterns, dependencies, dirs, confidence_with_match). Keep rules to file names and bounded content patterns. Report conflicting evidence instead of choosing silently.

## 7. Runtime tunables versus build-time changes
Runtime: none. Build-time: the rules file is data and can be extended without code changes.

## 8. Hardware-dependent decisions (/race lens) versus universal changes (/optimize lens) versus network-aware changes (/ping-optimize lens)
/race lens: detected architecture hints (for example arm64 base images) only become facts after verification. /optimize lens: uses detection only to know which build and deploy files exist, never to pick host-specific optimizations. /ping-optimize lens: detected platforms hint at edge, CDN and protocol support but are not proof.

## 9. Compatibility and version considerations
Rules are heuristics from general knowledge and have not been re-verified against current provider documentation (unverified, 2026-11-07). File conventions change; treat a missing match as unknown, not as absence.

## 10. Security, privacy and accessibility considerations
Detection is read-only, offline and bounded (depth, file count, bytes read per file). Output never includes file contents beyond matched names and signals. Collect only timings, counts, sizes and status codes. Never read, print or store secrets, tokens, connection strings, cookies or request/response bodies; redact them from logs and reports. Credentials come only from the developer's existing secret mechanism (environment, vault, cloud identity), never from chat. Keep telemetry local unless the developer authorizes export.

## 11. Validation and testing
tests/test_server_optimize.py runs the detector over six fixtures (managed hosting, Docker, Kubernetes, VPS, local development, multi-environment), asserts expected targets, confirms secrets in .env fixtures never appear in output, and confirms verified_live is false everywhere.

## 12. Rollback and failure handling
Make each change small and reversible with the previous behavior or configuration reachable (flag, config value or revert commit). Record a rollback point before editing. If validation fails, restore the last known-good state. Roll back only changes this workflow made, and only inside the authorized scope; never undo others' changes or touch live infrastructure to roll back without authorization.

## 13. Sources and last reviewed
General engineering practice; no external source was fetched for this file, so factual claims about specific products are unverified. Before relying on a platform limit, default or price, consult the provider's current official documentation and record the URL and access date here. Last reviewed: 2026-11-07.
