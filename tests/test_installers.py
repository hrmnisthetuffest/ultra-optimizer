"""Installer tests. All installs target a scratch dir; the real ~/.claude/skills is never touched."""
import os, subprocess, sys, tempfile, unittest, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INSTALL = ROOT / "install" / "install.sh"
UNINSTALL = ROOT / "install" / "uninstall.sh"


def run(script, *args, home, cwd=None, stdin=subprocess.DEVNULL):
    env = dict(os.environ, HOME=str(home))
    return subprocess.run(["bash", str(script), *args], env=env, cwd=cwd, text=True,
                          capture_output=True, stdin=stdin)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="uo-test-")
        self.home = pathlib.Path(self.tmp.name) / "home"
        self.skills = self.home / ".claude" / "skills"
        (self.skills / "unrelated").mkdir(parents=True)
        (self.skills / "unrelated" / "SKILL.md").write_text("---\nname: unrelated\n---\nkeep me\n")

    def tearDown(self):
        self.tmp.cleanup()

    def install(self, *a):
        return run(INSTALL, "--scope", "personal", *a, home=self.home)

    def test_fresh_install_and_unrelated_survives(self):
        r = self.install()
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((self.skills / "race" / "SKILL.md").is_file())
        self.assertTrue((self.skills / "optimize" / "SKILL.md").is_file())
        self.assertTrue((self.skills / "ping-optimize" / "SKILL.md").is_file())
        self.assertTrue((self.skills / "server-optimize" / "SKILL.md").is_file())
        self.assertEqual((self.skills / "unrelated" / "SKILL.md").read_text().splitlines()[-1], "keep me")
        self.assertTrue((self.skills / ".ultra-optimizer-manifest.tsv").is_file())

    def test_idempotent(self):
        self.install()
        r = self.install()
        self.assertIn("already up to date", r.stdout)
        self.assertFalse((self.skills / ".ultra-optimizer-backups").exists())

    def test_dry_run_changes_nothing(self):
        r = self.install("--dry-run")
        self.assertEqual(r.returncode, 0)
        self.assertFalse((self.skills / "race").exists())
        self.assertIn("dry run", r.stdout)

    def test_existing_differing_requires_yes_then_backs_up(self):
        (self.skills / "race").mkdir()
        (self.skills / "race" / "SKILL.md").write_text("someone else's race skill\n")
        r = self.install()
        self.assertIn("rerun with --yes", r.stdout)
        self.assertEqual((self.skills / "race" / "SKILL.md").read_text(), "someone else's race skill\n")
        r = self.install("--yes")
        self.assertEqual(r.returncode, 0, r.stderr)
        backups = list((self.skills / ".ultra-optimizer-backups").glob("*/race/SKILL.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "someone else's race skill\n")
        self.assertIn("name: race", (self.skills / "race" / "SKILL.md").read_text())

    def test_only_flag(self):
        self.install("--only", "optimize")
        self.assertTrue((self.skills / "optimize").is_dir())
        self.assertFalse((self.skills / "race").exists())

    def test_force_backup_on_identical(self):
        self.install()
        r = self.install("--force-backup", "--yes")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(list((self.skills / ".ultra-optimizer-backups").glob("*/race")))

    def test_uninstall_removes_only_owned_unmodified(self):
        self.install()
        mod = self.skills / "race" / "references" / "INDEX.md"
        mod.write_text(mod.read_text() + "\nuser edit\n")
        r = run(UNINSTALL, "--scope", "personal", home=self.home)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("references/INDEX.md", r.stdout)
        self.assertTrue(mod.is_file())
        self.assertFalse((self.skills / "race" / "SKILL.md").exists())
        self.assertFalse((self.skills / "optimize").exists())
        self.assertFalse((self.skills / "ping-optimize").exists())
        self.assertFalse((self.skills / "server-optimize").exists())
        self.assertTrue((self.skills / "unrelated" / "SKILL.md").is_file())

    def test_uninstall_without_manifest_is_noop(self):
        r = run(UNINSTALL, "--scope", "personal", home=self.home)
        self.assertIn("nothing removed", r.stdout)
        self.assertTrue((self.skills / "unrelated" / "SKILL.md").is_file())

    def test_path_with_space(self):
        target = pathlib.Path(self.tmp.name) / "a dir with space" / "skills"
        r = run(INSTALL, "--target", str(target), home=self.home)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue((target / "race" / "SKILL.md").is_file())

    def test_bad_args(self):
        self.assertEqual(run(INSTALL, "--scope", "bogus", home=self.home).returncode, 2)
        self.assertEqual(run(INSTALL, "--only", "x", home=self.home).returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
