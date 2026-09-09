"""Alignment 4-vector, A-star bounds, incompleteness guard, World."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any

__all__ = [
    "A_STAR",
    "Alignment",
    "DT_TICK",
    "ELL_MAX",
    "ELL_MID",
    "ELL_MIN",
    "EPS_C",
    "EPS_T",
    "LEAK_ZERO",
    "LIFE",
    "MOTTO",
    "N_PERSIST",
    "N_TERMINAL",
    "P_STAR",
    "P_STAR_VALUE",
    "Reject",
    "T_STAR",
    "C_STAR",
    "World",
    "apply",
    "guard",
    "pointer_p",
    "seed_world",
]

MOTTO = "Without correction, adaptation takes control."

T_STAR = 1.00
EPS_T = 0.08
C_STAR = 0.65
EPS_C = 0.10
ELL_MIN = 0.08
ELL_MAX = 0.32
ELL_MID = 0.20
LIFE: frozenset[int] = frozenset(range(8))
P_STAR: frozenset[int] = frozenset({0, 1, 2, 3})
P_STAR_VALUE = len(P_STAR) / len(LIFE)
LEAK_ZERO = 1e-12
N_PERSIST = 8
N_TERMINAL = 12
DT_TICK = 0.02

A_STAR = {
    "t": T_STAR,
    "eps_t": EPS_T,
    "c": C_STAR,
    "eps_c": EPS_C,
    "leak_min": ELL_MIN,
    "leak_max": ELL_MAX,
    "p": P_STAR_VALUE,
    "life_slots": len(LIFE),
}

Reject = str | None


def pointer_p(pointer: frozenset[int]) -> float:
    return len(pointer) / len(LIFE)


@dataclass(frozen=True)
class Alignment:
    """A = [time, coupling, leak, global_pointer]. Pointer lives on World."""

    time: float
    coupling: float
    leak: float

    def __post_init__(self) -> None:
        if not isinstance(self.time, (int, float)) or isinstance(self.time, bool):
            raise ValueError("time must be numeric")
        for name in ("coupling", "leak"):
            x = getattr(self, name)
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise ValueError(f"{name} must be numeric")
        if self.coupling < 0.0 or self.coupling > 1.0:
            raise ValueError(f"coupling must be in [0, 1], got {self.coupling}")
        if self.leak < 0.0 or self.leak > 1.0:
            raise ValueError(f"leak must be in [0, 1], got {self.leak}")


def guard(leak: float, pointer: frozenset[int]) -> Reject:
    """Reject writes that seal the system."""
    if leak < LEAK_ZERO:
        return "leak_zero"
    if pointer == LIFE:
        return "pointer_eq_life"
    if not pointer:
        return "pointer_eq_life"
    return None


_UNSET: Any = object()


def apply(
    world: World,
    *,
    time: float | None = None,
    coupling: float | None = None,
    leak: float | None = None,
    pointer: frozenset[int] | None = None,
    frozen: bool | None = None,
    r4_split: bool | None = None,
    scenario: Any = _UNSET,
) -> tuple[World, Reject]:
    """Propose a write. On reject, World is unchanged except ``reject``."""
    new_time = world.alignment.time if time is None else float(time)
    new_c = world.alignment.coupling if coupling is None else float(coupling)
    new_leak = world.alignment.leak if leak is None else float(leak)
    new_ptr = world.pointer if pointer is None else frozenset(pointer)
    reason = guard(new_leak, new_ptr)
    if reason:
        return replace(world, reject=reason), reason
    extra: dict[str, Any] = {}
    if frozen is not None:
        extra["frozen"] = frozen
    if r4_split is not None:
        extra["r4_split"] = r4_split
    if scenario is not _UNSET:
        extra["scenario"] = scenario
    al = Alignment(time=new_time, coupling=new_c, leak=new_leak)
    return replace(world, alignment=al, pointer=new_ptr, reject=None, **extra), None


@dataclass(frozen=True)
class World:
    alignment: Alignment
    pointer: frozenset[int]
    frozen: bool = False
    r4_split: bool = False
    mode: str = "CORRECTING"
    fault: str = "admissible"
    last_fault: str = "admissible"
    streak: int = 0
    tick: int = 0
    scenario: str | None = None
    locked_rank: str | None = None
    reject: Reject = None

    @staticmethod
    def seed(*, tick: int = 0) -> World:
        return World(
            alignment=Alignment(time=T_STAR, coupling=C_STAR, leak=0.18),
            pointer=P_STAR,
            tick=tick,
        )

    def residual(self) -> dict[str, float]:
        p = pointer_p(self.pointer)
        leak = self.alignment.leak
        if leak < ELL_MIN:
            dleak = leak - ELL_MIN
        elif leak > ELL_MAX:
            dleak = leak - ELL_MAX
        else:
            dleak = 0.0
        return {
            "dt": self.alignment.time - T_STAR,
            "dc": self.alignment.coupling - C_STAR,
            "dleak": dleak,
            "dp": p - P_STAR_VALUE,
        }

    def snapshot(self) -> dict[str, Any]:
        from .ranks import rank_views

        p = pointer_p(self.pointer)
        lamp = {
            "CORRECTING": "CORRECTING",
            "ADAPTING": "ADAPTATION HAS CONTROL",
            "TERMINAL": "TERMINAL",
        }[self.mode]
        a = self.alignment
        return {
            "tick": self.tick,
            "mode": self.mode,
            "lamp": lamp,
            "fault": self.fault,
            "streak": self.streak,
            "n_persist": N_PERSIST,
            "n_terminal": N_TERMINAL,
            "scenario": self.scenario,
            "reject": self.reject,
            "catalog_insufficient": True,
            "alignment": {"t": a.time, "c": a.coupling, "leak": a.leak, "p": p},
            "a_star": dict(A_STAR),
            "residual": self.residual(),
            "life": sorted(LIFE),
            "pointer": sorted(self.pointer),
            "frozen": self.frozen,
            "ranks": rank_views(self),
            "motto": MOTTO,
        }

    def tick_step(self) -> World:
        return self._advance(correct=False)

    def hold(self) -> World:
        return self._advance(correct=False)

    def correct(self) -> World:
        if self.mode == "TERMINAL":
            return replace(self, reject="terminal")
        from .adapt import note_fault
        from .correct import classify, run_correct

        w, _reason = run_correct(replace(self, reject=None))
        w = replace(w, fault=classify(w))
        return note_fault(w)

    def inject(self, scenario: str) -> World:
        if self.mode == "TERMINAL":
            return replace(self, reject="terminal")
        from .correct import classify
        from .scenarios import inject as inject_scenario

        try:
            w = inject_scenario(replace(self, reject=None), scenario)
        except ValueError:
            return replace(self, reject="unknown_scenario")
        w = replace(
            w,
            fault=classify(w),
            last_fault="admissible",
            streak=0,
            mode="CORRECTING",
            locked_rank=None,
            reject=None,
        )
        return w

    def reset(self) -> World:
        return World.seed()

    def _advance(self, *, correct: bool) -> World:
        if self.mode == "TERMINAL":
            return replace(self, reject="terminal")
        from .adapt import note_fault
        from .correct import classify
        from .scenarios import drift

        w = replace(self, tick=self.tick + 1, reject=None)
        w, reason = apply(w, time=w.alignment.time + DT_TICK)
        if reason:
            return replace(self, reject=reason)
        w = drift(w)
        w = replace(w, fault=classify(w))
        if correct:
            from .correct import run_correct

            w, _ = run_correct(w)
            w = replace(w, fault=classify(w))
        return note_fault(w)


def seed_world() -> World:
    return World.seed()
