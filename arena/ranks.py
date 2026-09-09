"""R1..R5 observations and native operators."""

from __future__ import annotations

from .state import (
    C_STAR,
    ELL_MAX,
    ELL_MID,
    ELL_MIN,
    EPS_C,
    EPS_T,
    LEAK_ZERO,
    LIFE,
    P_STAR,
    T_STAR,
    World,
    pointer_p,
)

__all__ = [
    "RANK_META",
    "admit_leak",
    "catastrophe",
    "merge_gradient",
    "rank_views",
    "rescue",
    "route",
    "seal",
    "split",
    "split_gradient",
    "tension_reset",
    "unroute",
]

RANK_META: tuple[tuple[str, str, str], ...] = (
    ("R1", "lattice-waveguide", "t"),
    ("R2", "energy surfaces", "c"),
    ("R3", "near-field network", "leak"),
    ("R4", "identity shell", "p"),
    ("R5", "boundary-scaffold", "tension"),
)


def rescue(time: float) -> float:
    return time + 0.5 * (T_STAR - time)


def catastrophe() -> float:
    return T_STAR


def merge_gradient(coupling: float) -> float:
    if coupling < C_STAR:
        return coupling + 0.5 * (C_STAR - coupling)
    return coupling


def split_gradient(coupling: float) -> float:
    if coupling > C_STAR:
        return coupling + 0.5 * (C_STAR - coupling)
    return coupling


def route(coupling: float) -> float:
    return min(1.0, coupling + 0.08)


def unroute(coupling: float) -> float:
    return max(0.0, coupling - 0.08)


def admit_leak(leak: float) -> float:
    new = leak + 0.5 * (ELL_MID - leak)
    if new < LEAK_ZERO:
        return LEAK_ZERO
    return new


def seal(pointer: frozenset[int]) -> frozenset[int] | None:
    """Add one LIFE slot. None = would equal life (reject)."""
    missing = sorted(LIFE - pointer)
    if not missing:
        return None
    nxt = pointer | {missing[0]}
    if nxt == LIFE:
        return None
    return nxt


def split(pointer: frozenset[int]) -> frozenset[int]:
    """Remove one slot. Stop at 1 (empty is illegal)."""
    if len(pointer) <= 1:
        return pointer
    drop = max(pointer)
    return pointer - {drop}


def tension_reset(world: World) -> dict:
    """Halfway to A-star. Unused by v0 correct (no escalate)."""
    a = world.alignment
    ptr = world.pointer
    if len(ptr) < len(P_STAR):
        sealed = seal(ptr)
        if sealed is not None:
            ptr = sealed
    elif len(ptr) > len(P_STAR):
        ptr = split(ptr)
    return {
        "time": a.time + 0.5 * (T_STAR - a.time),
        "coupling": a.coupling + 0.5 * (C_STAR - a.coupling),
        "leak": admit_leak(a.leak),
        "pointer": ptr,
    }


def _owned_residual(world: World, rank_id: str) -> bool:
    a = world.alignment
    if rank_id == "R1":
        return abs(a.time - T_STAR) > EPS_T
    if rank_id == "R2":
        return abs(a.coupling - C_STAR) > EPS_C
    if rank_id == "R3":
        return a.leak < ELL_MIN or a.leak > ELL_MAX or abs(a.coupling - C_STAR) > EPS_C
    if rank_id == "R4":
        return world.frozen or len(world.pointer) < len(P_STAR) or world.r4_split
    # R5: tension — any A-star miss
    p_ok = world.pointer != LIFE and bool(world.pointer)
    leak_ok = ELL_MIN <= a.leak <= ELL_MAX
    t_ok = abs(a.time - T_STAR) <= EPS_T
    c_ok = abs(a.coupling - C_STAR) <= EPS_C
    return not (t_ok and c_ok and leak_ok and p_ok and not world.frozen and not world.r4_split)


def _pip(world: World, rank_id: str) -> str:
    if world.locked_rank == rank_id:
        if world.mode == "TERMINAL":
            return "terminal"
        return "adapting"
    return "residual" if _owned_residual(world, rank_id) else "ok"


def rank_views(world: World) -> list[dict]:
    a = world.alignment
    p = pointer_p(world.pointer)
    rows = []
    for rank_id, name, owns in RANK_META:
        rows.append(
            {
                "id": rank_id,
                "name": name,
                "owns": owns,
                "t": a.time,
                "c": a.coupling,
                "leak": a.leak,
                "p": p,
                "pip": _pip(world, rank_id),
                "locked": world.locked_rank == rank_id,
            }
        )
    return rows
