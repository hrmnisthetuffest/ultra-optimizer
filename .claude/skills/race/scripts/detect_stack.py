#!/usr/bin/env python3
"""Deterministic stack detector for RACE reference routing (stdlib only).

Reads manifests/lockfiles/build files only (never source contents beyond manifests), and prints
which reference files are relevant. Anything not recognised is reported under "unknown" rather than guessed.
Usage: detect_stack.py PROJECT_DIR
"""
import json, os, sys

SKIP = {"node_modules", ".git", "target", "build", "dist", "__pycache__", ".venv", "venv"}
CORE = ["core/race-overview.md", "core/project-detection.md", "core/workload-analysis.md"]

# (signal, stack label, [reference files relative to references/])
FILE_RULES = {
    "Cargo.toml": ("rust", ["languages/rust.md"]),
    "go.mod": ("go", ["languages/go.md"]),
    "pubspec.yaml": ("flutter", ["frameworks/flutter-and-react-native.md"]),
    "CMakeLists.txt": ("cmake", ["languages/c-cpp.md", "compilers-and-build/compiler-optimization.md"]),
    "meson.build": ("meson", ["languages/c-cpp.md", "compilers-and-build/compiler-optimization.md"]),
    "pyproject.toml": ("python", ["languages/python.md"]),
    "requirements.txt": ("python", ["languages/python.md"]),
    "Package.swift": ("swift", ["languages/swift-objc.md"]),
    "pom.xml": ("java", ["languages/java-kotlin.md"]),
    "build.gradle": ("gradle", ["languages/java-kotlin.md"]),
    "build.gradle.kts": ("gradle", ["languages/java-kotlin.md"]),
    "tauri.conf.json": ("tauri", ["applications/tauri-apps.md", "languages/rust.md"]),
    "next.config.js": ("nextjs", ["frameworks/react-and-nextjs.md", "applications/websites-and-core-web-vitals.md"]),
    "next.config.mjs": ("nextjs", ["frameworks/react-and-nextjs.md", "applications/websites-and-core-web-vitals.md"]),
    "manage.py": ("django", ["frameworks/django-and-fastapi.md", "languages/python.md"]),
}
EXT_RULES = {".csproj": ("dotnet", ["languages/csharp-dotnet.md"]), ".sln": ("dotnet", ["languages/csharp-dotnet.md"]),
             ".xcodeproj": ("xcode", ["languages/swift-objc.md"]), ".pro": ("qmake", ["frameworks/qt-gtk-and-native-ui.md"])}
NPM_DEPS = {
    "electron": ("electron", ["applications/electron-apps.md", "languages/javascript-typescript.md"]),
    "react": ("react", ["frameworks/react-and-nextjs.md"]),
    "next": ("nextjs", ["frameworks/react-and-nextjs.md", "applications/websites-and-core-web-vitals.md"]),
    "express": ("node-backend", ["frameworks/nodejs-backend.md"]),
    "fastify": ("node-backend", ["frameworks/nodejs-backend.md"]),
    "typescript": ("typescript", ["languages/javascript-typescript.md"]),
    "better-sqlite3": ("sqlite", []), "sqlite3": ("sqlite", []),
    "react-native": ("react-native", ["frameworks/flutter-and-react-native.md"]),
    "@tauri-apps/api": ("tauri", ["applications/tauri-apps.md"]),
}
TEXT_HINTS = [  # (filename, substring, label, refs)
    ("CMakeLists.txt", "Qt", "qt", ["frameworks/qt-gtk-and-native-ui.md"]),
    ("CMakeLists.txt", "GTK", "gtk", ["frameworks/qt-gtk-and-native-ui.md"]),
    ("pyproject.toml", "fastapi", "fastapi", ["frameworks/django-and-fastapi.md"]),
    ("pyproject.toml", "django", "django", ["frameworks/django-and-fastapi.md"]),
    ("requirements.txt", "fastapi", "fastapi", ["frameworks/django-and-fastapi.md"]),
    ("requirements.txt", "django", "django", ["frameworks/django-and-fastapi.md"]),
    ("pom.xml", "spring", "spring", ["frameworks/spring-and-aspnet-core.md"]),
    ("Cargo.toml", "tauri", "tauri", ["applications/tauri-apps.md"]),
    ("Cargo.toml", "wgpu", "gpu-rendering", ["workloads/gpu-bound.md", "hardware/gpu-intelligence.md"]),
    ("pyproject.toml", "tkinter", "python-desktop", ["applications/desktop-apps.md"]),
    ("pyproject.toml", "PySide", "qt", ["frameworks/qt-gtk-and-native-ui.md", "applications/desktop-apps.md"]),
    ("pyproject.toml", "pandas", "data", ["workloads/memory-bound.md", "workloads/throughput-oriented.md"]),
    ("pyproject.toml", "numpy", "data", ["workloads/memory-bound.md", "workloads/throughput-oriented.md"]),
]
SPECIAL = [  # path-based signals
    ("ProjectSettings/ProjectVersion.txt", "unity", ["applications/games-and-game-launchers.md", "workloads/real-time.md", "workloads/gpu-bound.md", "languages/csharp-dotnet.md"]),
    ("pubspec.yaml", "flutter", ["frameworks/flutter-and-react-native.md", "workloads/latency-sensitive.md"]),
]
APP_KEYWORDS = {  # declared in a project-level hint file (optional): .race-hints.json {"kind": [...]}
    "browser": ["applications/browsers-and-browser-engines.md"],
    "messaging": ["workloads/network-bound.md", "workloads/latency-sensitive.md", "applications/desktop-apps.md"],
    "media-editor": ["workloads/gpu-bound.md", "workloads/throughput-oriented.md", "hardware/display-and-media-capabilities.md"],
}


def _json(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def _text(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def scan(root):
    found = {}
    unknown = []
    names = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP]
        if os.path.relpath(dp, root).count(os.sep) > 3:
            dn[:] = []
        for f in fn:
            names.append(os.path.join(dp, f))
    def add(label, refs):
        found.setdefault(label, set()).update(refs)
    for p in names:
        base = os.path.basename(p)
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        if base in FILE_RULES:
            add(*FILE_RULES[base])
        ext = os.path.splitext(base)[1]
        if ext in EXT_RULES:
            add(*EXT_RULES[ext])
        for sp, label, refs in SPECIAL:
            if rel.endswith(sp):
                add(label, refs)
        if base == "package.json":
            try:
                data = _json(p)
            except (OSError, ValueError):
                unknown.append(rel + " (unparseable)")
                continue
            deps = {}
            for k in ("dependencies", "devDependencies"):
                deps.update(data.get(k, {}))
            add("javascript", ["languages/javascript-typescript.md"])
            for d, (label, refs) in NPM_DEPS.items():
                if d in deps:
                    add(label, refs)
        if base in {h[0] for h in TEXT_HINTS}:
            try:
                txt = _text(p)
            except OSError:
                continue
            for fname, sub, label, refs in TEXT_HINTS:
                if base == fname and sub.lower() in txt.lower():
                    add(label, refs)
        if base == ".race-hints.json":
            try:
                for k in _json(p).get("kinds", []):
                    if k in APP_KEYWORDS:
                        add(k, APP_KEYWORDS[k])
                    else:
                        unknown.append("hint kind: " + str(k))
            except (OSError, ValueError):
                unknown.append(rel + " (unparseable)")
    if not found:
        unknown.append("no recognised manifest; ask the developer or inspect the build system manually")
    refs = list(CORE)
    for r in sorted({x for v in found.values() for x in v}):
        refs.append(r)
    return {"stack": sorted(found), "references": refs, "unknown": sorted(set(unknown))}


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print("usage: detect_stack.py PROJECT_DIR", file=sys.stderr)
        sys.exit(2)
    print(json.dumps(scan(sys.argv[1]), indent=2))
