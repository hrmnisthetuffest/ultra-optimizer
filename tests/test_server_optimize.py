"""Tests for the server-optimize subsystem: detection, intake, schemas, adaptation model, access rules."""
import json, subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SK = ROOT / ".claude" / "skills" / "server-optimize"
FIX = ROOT / "tests" / "fixtures" / "server"
sys.path.insert(0, str(SK / "templates"))
import server_adaptation_model as m  # noqa: E402


def detect(name, *extra):
    r = subprocess.run([sys.executable, "-I", str(SK / "scripts" / "detect_deployment.py"), str(FIX / name), *extra],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout), r.stdout


def validate(schema, rec):
    return subprocess.run([sys.executable, "-I", str(SK / "scripts" / "validate_records.py"),
                           str(SK / "schemas" / schema), str(SK / "schemas" / "examples" / rec)],
                          capture_output=True, text=True).returncode


class Detection(unittest.TestCase):
    def ids(self, name):
        d, _ = detect(name)
        return {t["id"] for t in d["targets"]}, d

    def test_managed(self):
        ids, d = self.ids("managed-vercel"); self.assertIn("vercel", ids)
    def test_docker(self):
        ids, _ = self.ids("docker-app"); self.assertIn("docker", ids)
    def test_k8s(self):
        ids, _ = self.ids("k8s-app"); self.assertIn("kubernetes", ids)
    def test_vps(self):
        ids, _ = self.ids("vps-app"); self.assertIn("vps-self-hosted", ids)
    def test_local_has_no_targets(self):
        ids, _ = self.ids("local-dev"); self.assertEqual(ids, set())
    def test_multi_env(self):
        ids, d = self.ids("multi-env"); self.assertTrue({"render", "fly-io"} <= ids)
        self.assertGreaterEqual(len(d.get("environment_hints", [])), 2)
    def test_never_claims_verified_live(self):
        for n in ("managed-vercel", "docker-app", "k8s-app", "vps-app", "multi-env"):
            d, _ = detect(n)
            for t in d["targets"]:
                self.assertFalse(t["verified_live"], n)
    def test_secret_values_never_leak(self):
        for p in FIX.iterdir():
            _, out = detect(p.name); _, out2 = detect(p.name, "--intake")
            self.assertNotIn("fixture-do-not-read", out); self.assertNotIn("fixture-do-not-read", out2)


class Intake(unittest.TestCase):
    EXPECT = {"mode", "environments", "hosting", "runtime", "services", "priorities", "workload",
              "access_level", "analysis_scope", "constraints"}
    def test_ten_items_one_batch_no_secret_field(self):
        for n in ("managed-vercel", "local-dev", "multi-env"):
            d, out = detect(n, "--intake")
            ids = {i["id"] for i in d["intake"]["items"]}
            self.assertEqual(ids, self.EXPECT)
            low = out.lower()
            for bad in ("password", "api_key", "secret_value"):
                self.assertNotIn(bad, [i["id"] for i in d["intake"]["items"]])
            self.assertIn("confirm_or_correct", d["intake"])

    def test_skill_demands_intake_first_and_default_repo_only(self):
        t = (SK / "SKILL.md").read_text()
        self.assertIn("--intake", t); self.assertIn("repo-only", t)
        self.assertIn("disable-model-invocation: true", t)


class Schemas(unittest.TestCase):
    def test_valid_and_invalid(self):
        self.assertEqual(validate("deployment-profile.schema.json", "valid-custom-profile.json"), 0)
        self.assertEqual(validate("deployment-profile.schema.json", "invalid-profile.json"), 1)
        self.assertEqual(validate("server-adaptation-policy.schema.json", "valid-adaptation-policy.json"), 0)
        self.assertEqual(validate("server-adaptation-policy.schema.json", "invalid-adaptation-policy.json"), 1)


class AdaptationModel(unittest.TestCase):
    POLICY = json.loads((SK / "schemas" / "examples" / "valid-adaptation-policy.json").read_text())

    def test_source_tracked_inputs(self):
        self.assertTrue(hasattr(m, "Controller") and hasattr(m, "plan") and hasattr(m, "Capabilities"))

    def test_out_of_range_override_rejected(self):
        caps = m.Capabilities(vcpus=(4, "verified-live"), mem_mb=(2048, "verified-live"))
        with self.assertRaises(ValueError):
            m.plan(self.POLICY, caps, 1, {"http_workers": 10 ** 6})

    def test_controller_restores_last_good(self):
        c = m.Controller({"workers": 2})
        c.apply({"workers": 4}, lambda p: True)
        ok = c.apply({"workers": 8}, lambda p: False)
        self.assertFalse(ok); self.assertEqual(c.current["workers"], 4)


class Boundaries(unittest.TestCase):
    def test_access_default_and_prod_gate(self):
        t = (SK / "references" / "deployment" / "access-levels-and-authorization.md").read_text().lower()
        for k in ("repo-only", "production-modify", "explicit", "migration", "firewall", "restart"):
            self.assertIn(k, t)

    def test_no_secrets_in_skill_instructions(self):
        t = (SK / "SKILL.md").read_text().lower()
        self.assertIn("secret", t)


if __name__ == "__main__":
    unittest.main()
