"""Generator is always plus. TOE manuscript imports are refused."""

from __future__ import annotations

import importlib
import sys

import pytest

from arena.generator import GENERATOR, GENERATOR_SIGN, mix


def test_generator_is_plus_never_minus() -> None:
    assert GENERATOR_SIGN == "+"
    assert "+" in GENERATOR
    assert "−" not in GENERATOR
    assert " - " not in GENERATOR
    assert mix(1.0, 1.0, 1.0) == 2.0
    assert mix(1.0, 1.0, 1.0) != mix(1.0, 1.0, -1.0)


def test_quiet_sign_flip_is_not_the_mix() -> None:
    q_o, sigma, q_c = 0.4, 0.7, 0.3
    plus = mix(q_o, sigma, q_c)
    minus = q_o - sigma * q_c
    assert plus != minus


@pytest.mark.parametrize("name", ["toe", "hfb", "mystery"])
def test_refuses_toe_manuscript_modules(name: str) -> None:
    import arena  # noqa: F401

    with pytest.raises(ImportError, match="refuses to import"):
        importlib.import_module(name)
    assert name not in sys.modules
