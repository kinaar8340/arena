"""Guard + one scenario per fault class + hold → adaptation."""

from __future__ import annotations

from dataclasses import replace

from arena.ranks import admit_leak, seal
from arena.state import (
    ELL_MAX,
    ELL_MIN,
    EPS_T,
    LIFE,
    P_STAR,
    World,
    apply,
    pointer_p,
)


def _correct_until(world: World, pred, cap: int = 8) -> World:
    for _ in range(cap):
        if pred(world):
            return world
        nxt = world.correct()
        if nxt.reject in {"rank_locked", "terminal"}:
            return nxt
        world = nxt
    return world


def test_guard_rejects_leak_zero() -> None:
    world = World.seed()
    before = world.alignment.leak
    out, reason = apply(world, leak=0.0)
    assert reason == "leak_zero"
    assert out.alignment.leak == before
    assert out.alignment.leak > 0.0
    assert out.pointer == world.pointer


def test_guard_rejects_pointer_eq_life() -> None:
    seven = LIFE - {7}
    assert seal(seven) is None
    world = replace(World.seed(), pointer=seven)
    out, reason = apply(world, pointer=LIFE)
    assert reason == "pointer_eq_life"
    assert out.pointer == seven
    assert out.pointer != LIFE
    assert out.pointer < LIFE


def test_admit_leak_never_writes_zero() -> None:
    assert admit_leak(0.02) > 0.0
    assert admit_leak(1e-9) >= 1e-12


def test_clock_drift_corrects() -> None:
    world = World.seed().inject("clock_drift")
    assert world.fault == "clock_drift"
    world = _correct_until(world, lambda w: w.fault == "admissible")
    assert world.fault == "admissible"
    assert abs(world.residual()["dt"]) <= EPS_T
    assert world.mode == "CORRECTING"


def test_denied_leak_corrects() -> None:
    world = World.seed().inject("denied_leak")
    assert world.fault == "denied_leak"
    leaks = [world.alignment.leak]
    world = _correct_until(world, lambda w: ELL_MIN <= w.alignment.leak <= ELL_MAX)
    leaks.append(world.alignment.leak)
    assert all(x > 0.0 for x in leaks)
    assert ELL_MIN <= world.alignment.leak <= ELL_MAX
    assert world.fault in {"admissible", "clock_drift", "energy_mismatch"}
    assert world.mode == "CORRECTING"


def test_frozen_pointer_corrects() -> None:
    world = World.seed().inject("frozen_pointer")
    assert world.fault == "frozen_pointer"
    assert world.frozen
    start_p = pointer_p(world.pointer)
    world = _correct_until(
        world,
        lambda w: (not w.frozen) and pointer_p(w.pointer) > start_p,
    )
    assert not world.frozen
    assert pointer_p(world.pointer) > start_p
    assert world.pointer != LIFE
    assert world.pointer < LIFE


def test_r4_split_corrects() -> None:
    world = World.seed().inject("r4_split")
    assert world.fault == "unlock"
    assert len(world.pointer) == 1
    world = _correct_until(world, lambda w: len(w.pointer) >= 2)
    assert len(world.pointer) >= 2
    assert world.pointer != LIFE
    assert world.pointer < LIFE
    assert abs(world.residual()["dt"]) <= EPS_T
    assert ELL_MIN <= world.alignment.leak <= ELL_MAX


def test_hold_without_correct_adapts_rank() -> None:
    world = World.seed().inject("clock_drift")
    for _ in range(8):
        world = world.hold()
    assert world.mode == "ADAPTING"
    assert world.locked_rank == "R1"
    ranks = {row["id"]: row for row in world.snapshot()["ranks"]}
    assert ranks["R1"]["pip"] == "adapting"
    assert ranks["R1"]["locked"] is True
    assert world.snapshot()["lamp"] == "ADAPTATION HAS CONTROL"


def test_hold_further_goes_terminal() -> None:
    world = World.seed().inject("clock_drift")
    for _ in range(12):
        world = world.hold()
    assert world.mode == "TERMINAL"
    assert world.correct().reject == "terminal"
    assert world.inject("denied_leak").reject == "terminal"
    reset = world.reset()
    assert reset.mode == "CORRECTING"
    assert reset.fault == "admissible"
    assert reset.locked_rank is None


def test_seed_is_admissible() -> None:
    world = World.seed()
    snap = world.snapshot()
    assert snap["fault"] == "admissible"
    assert snap["catalog_insufficient"] is True
    assert snap["alignment"]["p"] == pointer_p(P_STAR)
    assert 0.0 < snap["alignment"]["leak"] < 1.0
    assert set(snap["pointer"]) < set(snap["life"])
