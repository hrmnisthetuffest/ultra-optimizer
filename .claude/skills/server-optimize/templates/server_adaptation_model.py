"""Reference model: bounded application-level adaptation to VERIFIED server capabilities.

This is an executable contract, not universal runtime code. Port the rules to
the application's language. It never touches OS, kernel, network or
infrastructure settings: it only computes application parameters that a
developer-approved policy permits.

Rules enforced:
- no approved policy -> built-in defaults only;
- a derived value needs a VERIFIED capability, otherwise the policy default;
- every result is clamped into the developer's [min, max];
- a manual override outside [min, max] is rejected, not clamped silently;
- a failed validation restores the last known-good parameters;
- the sum of database pools across instances never exceeds the usable share
  of the database connection limit.
"""
import math

BASIS = {"effective_vcpus": "vcpus", "memory_limit_mb": "memory_mb", "db_max_connections": "db_max_connections",
         "downstream_capacity": "downstream_capacity"}


class Capabilities(object):
    """Capabilities with provenance. Only source == 'verified' values may drive adaptation."""

    def __init__(self, **facts):
        self.facts = facts  # name -> (value, source)

    def verified(self, name):
        v = self.facts.get(name)
        return v[0] if v and v[1] == "verified" and v[0] is not None and v[0] > 0 else None


def derive(param, caps, instances=1):
    """Return (value, reason) for one policy parameter."""
    lo, hi, default = param["min"], param["max"], param["default"]
    basis = param["derived_from"]
    if basis == "fixed":
        return _clamp(default, lo, hi), "fixed"
    cap = caps.verified(BASIS[basis])
    if cap is None:
        return _clamp(default, lo, hi), "capability not verified: using default"
    base = cap * param.get("fraction", 1.0)
    base *= 1.0 - param.get("safety_margin_fraction", 0.0)
    if param["kind"] == "db_pool_size":
        base = base / max(1, instances)
    value = math.floor(base)
    return _clamp(value, lo, hi), "derived from verified %s" % basis


def _clamp(v, lo, hi):
    return max(lo, min(hi, v))


def plan(policy, caps, instances=1, overrides=None):
    """Compute parameters. Returns (params, log). Raises ValueError on a rejected override."""
    log = []
    if not policy or policy.get("approved_by_developer") is not True:
        return {}, ["no approved policy: no adaptation performed"]
    params = {}
    overrides = overrides or {}
    for p in policy["parameters"]:
        value, why = derive(p, caps, instances)
        if p["name"] in overrides:
            o = overrides[p["name"]]
            if not (p["min"] <= o <= p["max"]):
                raise ValueError("override for %s outside approved range [%s, %s]" % (p["name"], p["min"], p["max"]))
            value, why = o, "developer override"
        params[p["name"]] = value
        log.append("%s=%s (%s)" % (p["name"], value, why))
    return params, log


class Controller(object):
    """Applies parameters, validates, and restores last-known-good on failure."""

    def __init__(self, defaults):
        self.last_good = dict(defaults)
        self.current = dict(defaults)

    def apply(self, params, validate):
        candidate = dict(self.current)
        candidate.update(params)
        if validate(candidate):
            self.current = candidate
            self.last_good = dict(candidate)
            return True
        self.current = dict(self.last_good)  # automatic rollback of our own change
        return False


def db_pool_total_ok(pool_per_instance, instances, db_max_connections, usable_fraction=0.8):
    return pool_per_instance * instances <= math.floor(db_max_connections * usable_fraction)
