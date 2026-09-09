"""Four canned faults: clock drift, denied leak, frozen pointer, R4 split."""

from __future__ import annotations

from dataclasses import replace

from .ranks import split
from .state import LEAK_ZERO, T_STAR, World, apply

__all__ = ["SCENARIOS", "drift", "inject"]

SCENARIOS = frozenset({"clock_drift", "denied_leak", "frozen_pointer", "r4_split"})


def inject(world: World, key: str) -> World:
    if key not in SCENARIOS:
        raise ValueError("unknown_scenario")
    base = World.seed(tick=world.tick)
    if key == "clock_drift":
        w, reason = apply(base, time=T_STAR + 0.40, scenario=key)
    elif key == "denied_leak":
        w, reason = apply(base, leak=0.02, scenario=key)
    elif key == "frozen_pointer":
        w, reason = apply(base, pointer=frozenset({0, 1}), frozen=True, scenario=key)
    else:
        ptr = base.pointer
        while len(ptr) > 1:
            ptr = split(ptr)
        w, reason = apply(base, pointer=ptr, r4_split=True, scenario=key)
    if reason:
        return replace(base, reject=reason, scenario=key)
    return w


def drift(world: World) -> World:
    """Scenario walk on tick/hold so skipping correction gets worse."""
    key = world.scenario
    a = world.alignment
    if key == "clock_drift":
        delta = 0.05 if a.time >= T_STAR else -0.05
        w, reason = apply(world, time=a.time + delta)
        return world if reason else w
    if key == "denied_leak":
        nxt = max(LEAK_ZERO * 10, a.leak - 0.01)
        w, reason = apply(world, leak=nxt)
        return world if reason else w
    if key == "frozen_pointer":
        return world
    if key == "r4_split":
        ptr = split(world.pointer)
        w, reason = apply(world, pointer=ptr, r4_split=True)
        return world if reason else w
    return world
