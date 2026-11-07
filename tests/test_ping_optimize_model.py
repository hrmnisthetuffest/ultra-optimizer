#!/usr/bin/env python3
"""Runnable checks for the /ping-optimize reference model and simulator (stdlib only)."""
import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SK = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "ping-optimize"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


sim = load("network_sim", SK / "templates" / "network_sim.py")
mdl = load("network_reference_model", SK / "templates" / "network_reference_model.py")


class Backoff(unittest.TestCase):
    def test_bounds_and_jitter(self):
        rng = random.Random(3)
        vals = [mdl.backoff_delay_ms(a, 100, 5000, rng) for a in range(12) for _ in range(20)]
        self.assertTrue(all(0 <= v <= 5000 for v in vals))
        self.assertGreater(len(set(round(v, 3) for v in vals)), 50)  # jittered, not fixed

    def test_negative_attempt_rejected(self):
        with self.assertRaises(ValueError):
            mdl.backoff_delay_ms(-1)


class Retry(unittest.TestCase):
    def test_non_idempotent_without_key_not_retried(self):
        net = sim.SimNetwork(sim.Profile(loss=1.0))
        r, n = mdl.call_with_retry(net, "POST")
        self.assertEqual(n, 1)
        self.assertEqual(net.requests, 1)

    def test_idempotent_retry_is_bounded_no_infinite_loop(self):
        net = sim.SimNetwork(sim.Profile(loss=1.0))
        r, n = mdl.call_with_retry(net, "GET", max_attempts=4)
        self.assertEqual(n, 4)
        self.assertEqual(net.requests, 4)

    def test_dns_failure_bounded(self):
        net = sim.SimNetwork(sim.Profile(dns_fail=True))
        r, n = mdl.call_with_retry(net, "GET", max_attempts=3)
        self.assertEqual((r.error, n), ("dns", 3))

    def test_post_with_key_applies_once_when_server_dedupes(self):
        net = sim.SimNetwork(sim.Profile(error_rate=0.6), seed=7)
        for i in range(30):
            mdl.call_with_retry(net, "POST", key=f"k{i}", max_attempts=6)
            # replay of the same key (e.g. client lost the response) must not double-apply
            net.request("POST", key=f"k{i}", dedupe_on_server=True)
        self.assertTrue(all(c == 1 for c in net.applied.values()), net.applied)

    def test_recovers_after_outage(self):
        net = sim.SimNetwork(sim.Profile(outages=[(0, 1500)]))
        r, n = mdl.call_with_retry(net, "GET", max_attempts=6)
        self.assertEqual(r.status, 200)

    def test_retry_after_honored_and_no_storm(self):
        net = sim.SimNetwork(sim.Profile(rate_limit_after=2))
        t0 = net.now_ms
        r, n = mdl.call_with_retry(net, "GET", max_attempts=1)
        r, n = mdl.call_with_retry(net, "GET", max_attempts=1)
        r, n = mdl.call_with_retry(net, "GET", max_attempts=3)
        self.assertLessEqual(net.requests, 5)
        self.assertGreaterEqual(net.now_ms - t0, 2000)  # waited per Retry-After

    def test_shared_budget_caps_layered_retries(self):
        net = sim.SimNetwork(sim.Profile(loss=1.0))
        b = mdl.RetryBudget(2)
        for _ in range(5):
            mdl.call_with_retry(net, "GET", max_attempts=10, budget=b)
        self.assertLessEqual(net.requests, 5 + 2)


class Concurrency(unittest.TestCase):
    def test_bounded_and_decreases_fast(self):
        c = mdl.AdaptiveConcurrency(lo=1, hi=6, start=4, dwell=2)
        for _ in range(50):
            c.observe(50, False)
        self.assertEqual(c.cur, 6)
        c.observe(50, True)
        self.assertEqual(c.cur, 3)
        for _ in range(100):
            c.observe(500, False)
        self.assertEqual(c.cur, 1)

    def test_high_bandwidth_alone_does_not_raise(self):
        c = mdl.AdaptiveConcurrency(lo=1, hi=8, start=2, dwell=3)
        c.observe(100, False)
        for _ in range(10):
            c.observe(400, False)  # latency growth, whatever the throughput
        self.assertLessEqual(c.cur, 2)

    def test_hysteresis_no_flap(self):
        c = mdl.AdaptiveConcurrency(lo=1, hi=8, start=4, dwell=4)
        seq = []
        for i in range(40):
            seq.append(c.observe(50, False))
        self.assertTrue(all(b - a <= 1 for a, b in zip(seq, seq[1:])))


class Classify(unittest.TestCase):
    def test_labels(self):
        ok = [20] * 10
        self.assertEqual(mdl.classify([20] * 3, [0], [0]), "unknown")
        self.assertEqual(mdl.classify(ok, [0] * 10, [0] * 10), "fast-stable")
        self.assertEqual(mdl.classify([150] * 10, [0] * 10, [0] * 10), "slow")
        self.assertEqual(mdl.classify([400] * 10, [0] * 10, [0] * 10), "high-latency")
        self.assertEqual(mdl.classify(ok, [1] * 5 + [0] * 5, [0] * 10), "lossy")
        self.assertEqual(mdl.classify([20] * 8 + [900] * 2, [0] * 10, [0] * 10), "unstable")


class SingleFlight(unittest.TestCase):
    def test_distinct_identity_keys_not_shared(self):
        sf = mdl.SingleFlight()
        a = sf.do(("userA", "/me"), lambda: "A")
        b = sf.do(("userB", "/me"), lambda: "B")
        self.assertEqual((a, b), ("A", "B"))


class Sim(unittest.TestCase):
    def test_deterministic(self):
        def run():
            n = sim.SimNetwork(sim.Profile(latency_ms=30, jitter_ms=10, loss=0.2), seed=5)
            return [(r.status, round(r.elapsed_ms, 3)) for r in (n.request() for _ in range(20))]
        self.assertEqual(run(), run())

    def test_bandwidth_cap_slows_large_payload(self):
        n = sim.SimNetwork(sim.Profile(latency_ms=10, bandwidth_kbps=800))
        small = n.request("POST", key="a", payload=b"x" * 100).elapsed_ms
        big = n.request("POST", key="b", payload=b"x" * 100000).elapsed_ms
        self.assertGreater(big, small * 10)

    def test_slow_server_is_not_rtt(self):
        n = sim.SimNetwork(sim.Profile(latency_ms=10, server_ms=500))
        r = n.request()
        self.assertGreaterEqual(r.elapsed_ms, 510)


class Detect(unittest.TestCase):
    def test_detects_hints_in_scratch_project(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "a.js").write_text("const ws = new WebSocket('wss://x'); fetch('/api'); // chat message")
            out = subprocess.run([sys.executable, "-I", str(SK / "scripts" / "detect_network_stack.py"), d],
                                 capture_output=True, text=True, check=True).stdout
            j = json.loads(out)
            self.assertIn("websocket", j["protocol_hints"])
            self.assertIn("fetch/axios/ky/got", j["libraries"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
