"""Correction: residuals → first-match classify → lowest competent rank."""

from __future__ import annotations

from dataclasses import replace

from .ranks import admit_leak, merge_gradient, rescue, seal, split, split_gradient, unroute
from .state import (
    C_STAR,
    ELL_MAX,
    ELL_MIN,
    EPS_C,
    EPS_T,
    P_STAR,
    T_STAR,
    World,
    apply,
)

__all__ = [
    "COMPETENT",
    "FAULTS",
    "classify",
    "run_correct",
]

FAULTS = (
    "frozen_pointer",
    "denied_leak",
    "runaway_leak",
    "unlock",
    "clock_drift",
    "energy_mismatch",
    "admissible",
)

COMPETENT: dict[str, str] = {
    "frozen_pointer": "R4",
    "denied_leak": "R3",
    "runaway_leak": "R3",
    "unlock": "R4",
    "clock_drift": "R1",
    "energy_mismatch": "R2",
}


def classify(world: World) -> str:
    """First match. Order is the law."""
    a = world.alignment
    if world.frozen:
        return "frozen_pointer"
    if a.leak < ELL_MIN:
        return "denied_leak"
    if a.leak > ELL_MAX:
        return "runaway_leak"
    if len(world.pointer) < len(P_STAR) or world.r4_split:
        return "unlock"
    if abs(a.time - T_STAR) > EPS_T:
        return "clock_drift"
    if abs(a.coupling - C_STAR) > EPS_C:
        return "energy_mismatch"
    return "admissible"


def _nudge_pointer_toward_star(pointer: frozenset[int]) -> frozenset[int]:
    if len(pointer) < len(P_STAR):
        nxt = seal(pointer)
        return pointer if nxt is None else nxt
    if len(pointer) > len(P_STAR):
        return split(pointer)
    return pointer


def _act(world: World, fault: str) -> dict:
    a = world.alignment
    if fault == "frozen_pointer":
        ptr = _nudge_pointer_toward_star(world.pointer)
        if ptr == world.pointer:
            # at p* but frozen: split to unstick, next correct seals back
            ptr = split(world.pointer)
        return {"pointer": ptr, "frozen": False}
    if fault == "denied_leak":
        return {"leak": admit_leak(a.leak)}
    if fault == "runaway_leak":
        if a.coupling > C_STAR:
            return {"coupling": unroute(a.coupling)}
        return {"leak": admit_leak(a.leak)}
    if fault == "unlock":
        nxt = seal(world.pointer)
        updates: dict = {}
        if nxt is not None:
            updates["pointer"] = nxt
            if len(nxt) >= len(P_STAR):
                updates["r4_split"] = False
        return updates
    if fault == "clock_drift":
        return {"time": rescue(a.time)}
    if fault == "energy_mismatch":
        if a.coupling < C_STAR:
            return {"coupling": merge_gradient(a.coupling)}
        return {"coupling": split_gradient(a.coupling)}
    return {}


def run_correct(world: World) -> tuple[World, str | None]:
    fault = classify(world)
    world = replace(world, fault=fault, reject=None)
    if fault == "admissible":
        return world, None
    rank = COMPETENT[fault]
    if world.locked_rank == rank:
        return replace(world, reject="rank_locked"), "rank_locked"
    proposed = _act(world, fault)
    if not proposed:
        return world, None
    w, reason = apply(world, **proposed)
    if reason:
        return w, reason
    w = replace(w, fault=classify(w), reject=None)
    return w, None
