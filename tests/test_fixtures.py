"""Tests deterministic stack detection against the 18.2 classification fixtures."""
import importlib.util, json, pathlib, unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SK = ROOT / ".claude" / "skills" / "race"
spec = importlib.util.spec_from_file_location("detect_stack", SK / "scripts" / "detect_stack.py")
ds = importlib.util.module_from_spec(spec); spec.loader.exec_module(ds)
FIX = ROOT / "tests" / "fixtures"
EXP = json.loads((FIX / "expected.json").read_text())


class T(unittest.TestCase):
    def test_all_fixtures(self):
        self.assertGreaterEqual(len(EXP), 11)
        for name, e in EXP.items():
            with self.subTest(name):
                out = ds.scan(str(FIX / name))
                for r in e["must_include"]:
                    self.assertIn(r, out["references"])
                for r in e["must_exclude"]:
                    self.assertNotIn(r, out["references"])
                for s in e["unknown_contains"]:
                    self.assertTrue(any(s in u for u in out["unknown"]), out["unknown"])

    def test_every_selected_reference_exists(self):
        for name in EXP:
            for r in ds.scan(str(FIX / name))["references"]:
                self.assertTrue((SK / "references" / r).is_file(), r)

    def test_known_fixture_has_no_unknown(self):
        self.assertEqual(ds.scan(str(FIX / "cpp-qt"))["unknown"], [])


if __name__ == "__main__":
    unittest.main()
