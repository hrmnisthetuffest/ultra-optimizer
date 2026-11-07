"""Deterministic simulated network for condition tests (stdlib only).

ILLUSTRATIVE EXECUTABLE CONTRACT, not production code. It models a link with
latency, jitter, loss, bandwidth cap, outage windows, DNS failure, slow or
erroring server and partial responses, on a virtual clock so tests never sleep
and never touch the real network.
"""
import random


class Profile:
    def __init__(self, latency_ms=20, jitter_ms=0, loss=0.0, bandwidth_kbps=0,
                 outages=(), dns_fail=False, server_ms=0, error_rate=0.0,
                 partial_rate=0.0, rate_limit_after=0):
        self.latency_ms = latency_ms
        self.jitter_ms = jitter_ms
        self.loss = loss
        self.bandwidth_kbps = bandwidth_kbps      # 0 = unlimited
        self.outages = list(outages)              # [(start_ms, end_ms)]
        self.dns_fail = dns_fail
        self.server_ms = server_ms
        self.error_rate = error_rate
        self.partial_rate = partial_rate
        self.rate_limit_after = rate_limit_after  # 429 after N requests (0 = off)


class Response:
    def __init__(self, status, body=b"", elapsed_ms=0, retry_after=None, error=None):
        self.status, self.body, self.elapsed_ms = status, body, elapsed_ms
        self.retry_after, self.error = retry_after, error


class SimNetwork:
    """Server records every applied (non-duplicate) side effect by idempotency key."""

    def __init__(self, profile, seed=1):
        self.p = profile
        self.rng = random.Random(seed)
        self.now_ms = 0
        self.requests = 0
        self.applied = {}          # key -> count of applications of a side effect
        self.log = []

    def _in_outage(self):
        return any(a <= self.now_ms < b for a, b in self.p.outages)

    def _delay(self, nbytes):
        d = self.p.latency_ms + (self.rng.uniform(-1, 1) * self.p.jitter_ms if self.p.jitter_ms else 0)
        if self.p.bandwidth_kbps:
            d += nbytes * 8 / self.p.bandwidth_kbps
        return max(0.0, d) + self.p.server_ms

    def request(self, method="GET", key=None, payload=b"", dedupe_on_server=False):
        self.requests += 1
        if self.p.dns_fail:
            self.now_ms += 5
            return Response(0, error="dns", elapsed_ms=5)
        if self._in_outage() or self.rng.random() < self.p.loss:
            self.now_ms += 1000  # client-side timeout
            return Response(0, error="timeout", elapsed_ms=1000)
        d = self._delay(len(payload))
        self.now_ms += d
        if self.p.rate_limit_after and self.requests > self.p.rate_limit_after:
            return Response(429, elapsed_ms=d, retry_after=2000)
        if self.rng.random() < self.p.error_rate:
            return Response(503, elapsed_ms=d)
        if method == "POST" and key is not None:
            if dedupe_on_server and key in self.applied:
                return Response(200, b"dup-ignored", d)
            self.applied[key] = self.applied.get(key, 0) + 1
        body = b"ok" if self.rng.random() >= self.p.partial_rate else b"o"  # truncated
        return Response(200, body, d)
