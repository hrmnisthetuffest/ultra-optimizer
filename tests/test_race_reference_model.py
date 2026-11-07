import importlib.util, pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("m", ROOT/".claude/skills/race/templates/race_reference_model.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

PARAMS = {
 "pool": {"type":"int","min":1,"max":16,"default":4},
 "path": {"type":"enum","values":["scalar","avx2"],"default":"scalar","requires":{"avx2"}},
 "cache": {"type":"bool","default":True},
}

class T(unittest.TestCase):
    def reg(self): return m.Registry(PARAMS)
    def test_out_of_range_rejected(self):
        with self.assertRaises(m.RegistryError): self.reg().validate({"pool":99})
    def test_bool_not_int(self):
        with self.assertRaises(m.RegistryError): self.reg().validate({"pool":True})
    def test_unregistered_rejected(self):
        with self.assertRaises(m.RegistryError): self.reg().validate({"evil":1})
    def test_unsupported_capability(self):
        with self.assertRaises(m.RegistryError): self.reg().validate({"path":"avx2"})
        self.assertTrue(self.reg().validate({"path":"avx2"}, {"avx2"}))
    def test_threshold_cumulative_foreground(self):
        s = m.Scheduler()
        s.tick(29*60, True); s.tick(10*3600, False)  # background time does not count
        self.assertFalse(s.may_run_deep_profile(idle=True))
        s.tick(60, True)
        self.assertTrue(s.may_run_deep_profile(idle=True))
    def test_not_interrupting_when_busy(self):
        s = m.Scheduler(); s.tick(3600, True)
        self.assertFalse(s.may_run_deep_profile(idle=False))
        self.assertFalse(s.may_run_deep_profile(idle=True, critical_state=True))
    def test_pause_on_user_activity_and_disable(self):
        s = m.Scheduler(); s.tick(3600, True)
        s.user_activity(); self.assertFalse(s.may_run_deep_profile(idle=True))
        s.resume(); self.assertTrue(s.may_run_deep_profile(idle=True))
        s.disabled = True; self.assertFalse(s.may_run_deep_profile(idle=True))
    def test_battery_thermal_abort(self):
        s = m.Scheduler(); s.tick(3600, True)
        self.assertFalse(s.may_run_deep_profile(idle=True, on_battery_saver=True))
        self.assertFalse(s.may_run_deep_profile(idle=True, thermal_ok=False))
    def test_apply_rollback_lkg_exact(self):
        e = m.Engine(self.reg()); base = dict(e.active)
        self.assertTrue(e.apply({"pool":8})); e.commit()
        self.assertTrue(e.apply({"pool":2}))
        e.rollback(); self.assertEqual(e.active["pool"], 8)
        e.restore_defaults(); self.assertEqual(e.active, base)
    def test_failed_validation_leaves_state(self):
        e = m.Engine(self.reg()); before = dict(e.active)
        self.assertFalse(e.apply({"pool":8}, validate_fn=lambda s: False))
        self.assertEqual(e.active, before)
    def test_invalid_apply_never_mutates(self):
        e = m.Engine(self.reg()); before = dict(e.active)
        with self.assertRaises(m.RegistryError): e.apply({"pool":1, "path":"avx2"})
        self.assertEqual(e.active, before)
if __name__ == "__main__": unittest.main()
