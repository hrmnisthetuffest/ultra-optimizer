"""RACE reference model: an EXECUTABLE CONTRACT, not universal runtime code.

Port these semantics to the host application's language. It demonstrates the
tuning-registry validation, the profiling scheduler gates and transactional
apply/rollback that the RACE references require. Stdlib only.
"""
import copy

CUMULATIVE_FOREGROUND_THRESHOLD_S = 30 * 60  # earliest point deeper profiling may be considered


class RegistryError(Exception):
    pass


class Registry:
    def __init__(self, params):
        # params: {id: {"type": "int"|"enum"|"bool", "min","max","values","default","requires":set}}
        self.params = params

    def validate(self, changes, capabilities=frozenset()):
        for pid, val in changes.items():
            p = self.params.get(pid)
            if p is None:
                raise RegistryError("unregistered parameter: %s" % pid)
            t = p["type"]
            if t == "int":
                if isinstance(val, bool) or not isinstance(val, int):
                    raise RegistryError("%s: not an int" % pid)
                if val < p["min"] or val > p["max"]:
                    raise RegistryError("%s: %r out of range" % (pid, val))
            elif t == "enum":
                if val not in p["values"]:
                    raise RegistryError("%s: %r not allowed" % (pid, val))
            elif t == "bool":
                if not isinstance(val, bool):
                    raise RegistryError("%s: not a bool" % pid)
            missing = set(p.get("requires", ())) - set(capabilities)
            if missing:
                raise RegistryError("%s: unsupported, needs %s" % (pid, sorted(missing)))
        return True

    def defaults(self):
        return {k: v["default"] for k, v in self.params.items()}


class Scheduler:
    """Gates deeper profiling/benchmarking. Time is injected by the caller."""

    def __init__(self, threshold_s=CUMULATIVE_FOREGROUND_THRESHOLD_S):
        self.threshold_s = threshold_s
        self.foreground_s = 0.0
        self.paused = False
        self.disabled = False

    def tick(self, seconds, foreground):
        if foreground:
            self.foreground_s += seconds

    def user_activity(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def may_run_deep_profile(self, idle, critical_state=False, on_battery_saver=False, thermal_ok=True):
        if self.disabled or self.paused or critical_state or not idle:
            return False
        if self.foreground_s < self.threshold_s:
            return False
        if on_battery_saver or not thermal_ok:
            return False
        return True


class Engine:
    """Transactional apply with last-known-good (LKG) and rollback."""

    def __init__(self, registry):
        self.registry = registry
        self.active = registry.defaults()
        self.lkg = copy.deepcopy(self.active)
        self.history = []

    def apply(self, changes, capabilities=frozenset(), validate_fn=None):
        self.registry.validate(changes, capabilities)  # raises before any mutation
        staged = {**self.active, **changes}
        if validate_fn is not None and not validate_fn(staged):
            self.history.append(("rejected", dict(changes)))
            return False
        self.active = staged
        self.history.append(("applied", dict(changes)))
        return True

    def commit(self):
        self.lkg = copy.deepcopy(self.active)

    def rollback(self):
        self.active = copy.deepcopy(self.lkg)
        self.history.append(("rolled_back", None))

    def restore_defaults(self):
        self.active = self.registry.defaults()
        self.lkg = copy.deepcopy(self.active)
        self.history.append(("restored_defaults", None))
