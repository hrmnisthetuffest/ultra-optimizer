#!/usr/bin/env python3
"""Heuristic first guess of a project's networking stack (stdlib only, read-only).

Usage: detect_network_stack.py PROJECT_ROOT
Prints JSON: detected libraries, protocols hints, and a likely application
category. This is a hint to verify by reading code, never a conclusion.
"""
import json
import os
import re
import sys

SKIP = {".git", "node_modules", "target", "dist", "build", "__pycache__", ".venv", "venv"}
LIBS = {
    "fetch/axios/ky/got": r"\b(fetch\(|axios|got\(|ky\()",
    "requests/httpx/aiohttp": r"\b(requests\.|httpx|aiohttp|urllib3)",
    "okhttp/retrofit": r"\b(OkHttp|Retrofit)",
    "libcurl": r"\bcurl_easy",
    "reqwest/hyper": r"\b(reqwest|hyper::)",
    "net/http (Go)": r"\"net/http\"",
    "HttpClient (.NET/Java)": r"\bHttpClient\b",
    "URLSession": r"\bURLSession\b",
    "grpc": r"\bgrpc\b",
}
PROTO = {
    "websocket": r"(?i)websocket|socket\.io|\bws://|\bwss://",
    "webrtc": r"(?i)RTCPeerConnection|webrtc",
    "udp": r"(?i)\bUDP\b|SOCK_DGRAM|UdpClient|DatagramSocket",
    "quic/http3": r"(?i)\bquic\b|http/?3",
    "sse": r"(?i)EventSource|text/event-stream",
    "polling": r"(?i)setInterval\(.*fetch|while\s*\(true\).*(sleep|poll)",
}
CATEGORY = {
    "game": r"(?i)\b(unity|unreal|godot|netcode|snapshot|tick ?rate|matchmak)",
    "browser/web": r"(?i)\b(react|vue|angular|next\.js|service ?worker|web ?vitals)",
    "messaging": r"(?i)\b(message|chat|xmpp|matrix)\b",
    "video-streaming": r"(?i)\b(hls|dash|m3u8|mpd|bitrate|rebuffer)",
    "downloads/sync": r"(?i)\b(download|upload|resum|chunk|rsync|sync)\b",
    "api/saas": r"(?i)\b(openapi|swagger|rest api|graphql)\b",
}
EXTS = (".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".kt", ".go", ".rs", ".c", ".cc", ".cpp", ".cs", ".swift", ".dart", ".rb", ".php", ".json", ".toml", ".md")


def scan(root):
    libs, proto, cat = {}, {}, {}
    n = 0
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP]
        for f in files:
            if not f.endswith(EXTS):
                continue
            p = os.path.join(d, f)
            try:
                if os.path.getsize(p) > 400_000:
                    continue
                t = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            n += 1
            for table, out in ((LIBS, libs), (PROTO, proto), (CATEGORY, cat)):
                for k, rx in table.items():
                    if re.search(rx, t):
                        out[k] = out.get(k, 0) + 1
            if n > 5000:
                break
    top = max(cat, key=cat.get) if cat else "unknown"
    return {"files_scanned": n, "libraries": libs, "protocol_hints": proto,
            "category_hints": cat, "likely_category": top,
            "note": "heuristic hints only; verify by reading the code"}


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        sys.exit("usage: detect_network_stack.py PROJECT_ROOT")
    print(json.dumps(scan(sys.argv[1]), indent=2, sort_keys=True))
