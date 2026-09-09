"""Takeover / lock-in / terminal after N persistent faults."""

from __future__ import annotations

from dataclasses import replace

from .correct import COMPETENT
from .state import N_PERSIST, N_TERMINAL, World

__all__ = ["note_fault"]


def note_fault(world: World) -> World:
    """Count persistence of the same non-admissible class. Adaptation is not success."""
    fault = world.fault
    if fault == "admissible":
        return replace(world, streak=0, last_fault="admissible")

    if fault == world.last_fault:
        streak = world.streak + 1
    else:
        streak = 1

    mode = world.mode
    locked = world.locked_rank
    if mode != "TERMINAL":
        if streak >= N_TERMINAL:
            mode = "TERMINAL"
            locked = locked or COMPETENT.get(fault)
        elif streak >= N_PERSIST:
            mode = "ADAPTING"
            locked = locked or COMPETENT.get(fault)

    return replace(
        world,
        streak=streak,
        last_fault=fault,
        mode=mode,
        locked_rank=locked,
    )
