"""Reference model of application-level network policy (stdlib only).

ILLUSTRATIVE EXECUTABLE CONTRACT, not universal runtime code. Adapt the logic
to the project's language and networking library. Nothing here touches the
real network, the OS or any device setting.
"""
import random

IDEMPOTENT = {"GET", "HEAD", "OPTIONS", "PUT", "DELETE"}


def backoff_delay_ms(attempt, base_ms=100, cap_ms=10000, rng=random):
    """Exponential backoff with full randomized jitter, bounded by cap."""
    if attempt < 0:
        raise ValueError("attempt must be >= 0")
    ceiling = min(cap_ms, base_ms * (2 ** attempt))
    return rng.uniform(0, ceiling)


class RetryBudget:
    """Caps total retries so layered retries cannot create a request storm."""

    def __init__(self, max_retries):
        self.left = max_retries

    def take(self):
        if self.left <= 0:
            return False
        self.left -= 1
        return True


def may_retry(method, has_idempotency_key):
    return method.upper() in IDEMPOTENT or bool(has_idempotency_key)


def call_with_retry(net, method, key=None, max_attempts=5, budget=None, rng=None,
                    sleep=None, **kw):
    """Retry transient failures. Non-idempotent calls retry only with a key.
    Honors Retry-After. Returns (response, attempts). Never loops forever."""
    rng = rng or random.Random(0)
    budget = budget or RetryBudget(max_attempts - 1)
    attempts = 0
    while True:
        attempts += 1
        r = net.request(method, key=key, **kw)
        transient = r.status in (0, 429, 503)
        if not transient or attempts >= max_attempts:
            return r, attempts
        if not may_retry(method, key) or not budget.take():
            return r, attempts
        wait = r.retry_after if r.retry_after else backoff_delay_ms(attempts - 1, rng=rng)
        net.now_ms += wait
        if sleep:
            sleep(wait)


class SingleFlight:
    """Coalesce identical in-flight requests; key MUST include identity context."""

    def __init__(self):
        self.inflight = {}

    def do(self, key, fn):
        if key in self.inflight:
            return self.inflight[key]
        self.inflight[key] = None
        try:
            res = fn()
            self.inflight[key] = res
            return res
        finally:
            self.inflight.pop(key, None)


class AdaptiveConcurrency:
    """AIMD concurrency with hard bounds and hysteresis. Never scales from
    bandwidth alone: only from observed errors and latency growth."""

    def __init__(self, lo=1, hi=8, start=2, dwell=3, lat_ratio=1.5):
        assert 1 <= lo <= start <= hi
        self.lo, self.hi, self.cur, self.dwell, self.lat_ratio = lo, hi, start, dwell, lat_ratio
        self.baseline = None
        self._good = 0

    def observe(self, latency_ms, error):
        if self.baseline is None and not error:
            self.baseline = latency_ms
        if error or (self.baseline and latency_ms > self.baseline * self.lat_ratio):
            self.cur = max(self.lo, self.cur // 2)       # fast decrease
            self._good = 0
        else:
            self._good += 1
            if self._good >= self.dwell:                 # slow increase after dwell
                self.cur = min(self.hi, self.cur + 1)
                self._good = 0
        return self.cur


def classify(rtts_ms, losses, errors):
    """Coarse condition label from rolling samples; 'unknown' if too few."""
    if len(rtts_ms) < 5:
        return "unknown"
    s = sorted(rtts_ms)
    p50, p95 = s[len(s) // 2], s[int(len(s) * 0.95) - 1]
    loss = sum(losses) / max(1, len(losses))
    err = sum(errors) / max(1, len(errors))
    if loss > 0.05:
        return "lossy"
    if err > 0.1 or p95 > 3 * p50:
        return "unstable"
    if p50 > 300:
        return "high-latency"
    if p50 > 100:
        return "slow"
    return "fast-stable"
