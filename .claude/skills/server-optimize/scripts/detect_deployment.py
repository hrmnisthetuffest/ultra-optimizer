#!/usr/bin/env python3
"""Detect deployment targets from repository files (stdlib only, read-only).

Usage: detect_deployment.py PROJECT_ROOT [--intake]
Prints JSON. Every result is REPOSITORY EVIDENCE with verified_live=false.
It never opens secret-bearing files (.env*, keys, credentials, tfstate,
kubeconfig) - only their names are used for environment hints - and never
touches the network. With --intake it also emits the consolidated intake
form with detectable answers prefilled.
"""
import fnmatch
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = {".git", "node_modules", "target", "dist", "build", "__pycache__", ".venv", "venv", ".next", "vendor"}
MAX_DEPTH = 6
MAX_READ = 65536
MAX_FILES = 20000
INTAKE_ITEMS = [
    ("mode", "Deployment mode: automatic detection, custom deployment, or local-only?", ["automatic", "custom", "local-only"]),
    ("environments", "Target environment(s): development, staging, production, or multiple?", ["development", "staging", "production", "multiple"]),
    ("hosting", "Hosting provider, platform and location/region (if any)?", None),
    ("runtime", "Runtime, language, CPU architecture and infrastructure details?", None),
    ("services", "Databases, caches, queues and external services involved?", None),
    ("priorities", "Optimization priorities (latency, throughput, cost, reliability, memory, cold-start, scalability)?", None),
    ("workload", "Expected workload and traffic characteristics?", None),
    ("access_level", "Available access level (none, read-only infra, read-only metrics, staging, production)?", None),
    ("analysis_scope", "Analysis scope: repository-only, read-only live analysis, or authorized implementation?", ["repository-only", "read-only-live", "authorized-implementation"]),
    ("constraints", "Operational constraints: downtime limits, migration limits, spending limits?", None),
]


def load_rules():
    with open(os.path.join(HERE, "detection-rules.json"), encoding="utf-8") as f:
        return json.load(f)


def is_sensitive(name, patterns):
    return any(re.search(p, name, re.I) for p in patterns)


def walk(root):
    root = os.path.abspath(root)
    n = 0
    for d, dirs, files in os.walk(root):
        depth = d[len(root):].count(os.sep)
        dirs[:] = sorted(x for x in dirs if x not in SKIP) if depth < MAX_DEPTH else []
        for f in sorted(files):
            n += 1
            if n > MAX_FILES:
                return
            yield os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/")
        for x in dirs:
            yield os.path.relpath(os.path.join(d, x), root).replace(os.sep, "/") + "/"


def read_head(root, rel):
    try:
        with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as f:
            return f.read(MAX_READ)
    except OSError:
        return ""


def package_deps(root, paths):
    deps = set()
    for p in paths:
        if os.path.basename(p) == "package.json":
            try:
                data = json.loads(read_head(root, p))
            except ValueError:
                continue
            for k in ("dependencies", "devDependencies"):
                deps.update((data.get(k) or {}).keys())
    return deps


def runtime_hints(paths):
    marks = {"package.json": "javascript/typescript", "pyproject.toml": "python", "requirements.txt": "python", "go.mod": "go",
             "Cargo.toml": "rust", "pom.xml": "java", "build.gradle": "java/kotlin", "Gemfile": "ruby", "composer.json": "php"}
    found = {}
    for p in paths:
        b = os.path.basename(p)
        if b in marks:
            found.setdefault(marks[b], []).append(p)
    return found


def detect(root):
    rules = load_rules()
    root = os.path.abspath(root)
    allp = list(walk(root))
    files = [p for p in allp if not p.endswith("/")]
    dirs = [p.rstrip("/") for p in allp if p.endswith("/")]
    sens = rules["sensitive_never_open"]
    deps = package_deps(root, files)
    targets, notes = [], []
    for t in rules["targets"]:
        ev = []
        for p in files:
            base = os.path.basename(p)
            if any(p == f or p.endswith("/" + f) for f in t["files"]):
                ev.append({"file": p, "signal": "file-name"})
            elif any(fnmatch.fnmatch(base, g) for g in t["globs"]):
                ev.append({"file": p, "signal": "file-glob"})
        for dname in t["dirs"]:
            for d in dirs:
                if os.path.basename(d) == dname:
                    ev.append({"file": d + "/", "signal": "directory"})
        for dep in t["dependencies"]:
            if dep in deps:
                ev.append({"file": "package.json", "signal": "dependency:" + dep})
        for fglob, rx in t["content"]:
            for p in files:
                if fnmatch.fnmatch(os.path.basename(p), fglob) and not is_sensitive(os.path.basename(p), sens):
                    if re.search(rx, read_head(root, p)):
                        ev.append({"file": p, "signal": "content-match"})
        if ev:
            seen, uniq = set(), []
            for e in ev:
                k = (e["file"], e["signal"])
                if k not in seen:
                    seen.add(k)
                    uniq.append(e)
            targets.append({"id": t["id"], "category": t["category"], "label": t["label"], "confidence": t["confidence_with_match"],
                            "evidence": uniq[:12], "status": "detected-from-repository", "verified_live": False, "note": t["note"]})
    envs = {}
    hints = rules["environment_hints"]
    for p in files:
        b = os.path.basename(p)
        for rx in hints["file_name_patterns"]:
            m = re.search(rx, b)
            if m:
                name = (m.group(1) if m.groups() else re.sub(r"[^a-z]", "", b.lower()))
                envs.setdefault(norm_env(name), []).append(p)
    for d in dirs:
        if os.path.basename(d) in hints["dir_names"]:
            for c in dirs:
                if os.path.dirname(c) == d and os.path.basename(c) in hints["dir_child_names"]:
                    envs.setdefault(norm_env(os.path.basename(c)), []).append(c + "/")
    for p in files:  # compose/fly names handled above; terraform tfvars
        m = re.search(r"(?:^|[-_.])(staging|production|prod|dev)\.(?:tfvars|ya?ml|json)$", os.path.basename(p))
        if m and not is_sensitive(os.path.basename(p), sens):
            envs.setdefault(norm_env(m.group(1)), []).append(p)
    content_envs = infer_env_from_services(root, files, sens)
    for k, v in content_envs.items():
        envs.setdefault(k, []).extend(v)
    env_list = [{"name": k, "evidence": sorted(set(v))[:8], "status": "detected-from-repository"} for k, v in sorted(envs.items())]
    if not targets:
        notes.append("No deployment configuration found in the repository; treat as local-only until the developer says otherwise.")
    result = {"schema": "ultra-optimizer/detected-deployment/1.0", "root_name": os.path.basename(root), "targets": targets,
              "environment_hints": env_list, "runtime_hints": runtime_hints(files), "notes": notes,
              "disclaimer": "Repository evidence only. Actual region, instance size and running configuration are unknown until verified by the developer or a read-only live check."}
    return result


def norm_env(n):
    n = n.lower()
    return {"prod": "production", "stage": "staging", "dev": "development", "local": "development"}.get(n, n)


def infer_env_from_services(root, files, sens):
    out = {}
    for p in files:
        if os.path.basename(p) == "render.yaml":
            text = read_head(root, p)
            for m in re.finditer(r"(?mi)^\s*-?\s*name:\s*\S*?[-_](staging|production|prod)\b", text):
                out.setdefault(norm_env(m.group(1)), []).append(p)
    return out


def intake(det):
    ts = det["targets"]
    ids = [t["id"] for t in ts]
    envs = [e["name"] for e in det["environment_hints"]]
    form, unresolved = [], []
    for key, q, options in INTAKE_ITEMS:
        pre, src = None, "needs-answer"
        if key == "mode":
            pre, src = ("automatic" if ts else "local-only"), "suggested-from-detection"
        elif key == "environments" and envs:
            pre, src = (envs if len(envs) > 1 else envs[0]), "detected-from-repository"
        elif key == "hosting" and ts:
            pre, src = ids, "detected-from-repository (unverified: region and plan unknown)"
        elif key == "runtime" and det["runtime_hints"]:
            pre, src = sorted(det["runtime_hints"].keys()), "detected-from-repository (version and CPU architecture unknown)"
        elif key == "access_level":
            pre, src = "repo-only", "safe-default"
        elif key == "analysis_scope":
            pre, src = "repository-only", "safe-default"
        item = {"id": key, "question": q, "options": options, "prefill": pre, "prefill_source": src,
                "answer_may_be": ["unknown", "not-applicable"], "status": "prefilled" if pre is not None else "needs-answer"}
        form.append(item)
        if item["status"] == "needs-answer" or src.startswith(("detected", "suggested")):
            unresolved.append(key)
    return {"schema": "ultra-optimizer/server-intake/1.0", "instructions": "Ask every item in ONE batch. Never ask for secrets or credentials.",
            "items": form, "confirm_or_correct": unresolved}


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1 or not os.path.isdir(args[0]):
        print(__doc__)
        return 2
    det = detect(args[0])
    out = det if "--intake" not in argv else {"detected": det, "intake": intake(det)}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
