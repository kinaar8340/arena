"""Locked mix. Model, not a QGA theorem.

Q = Q_O + σ(Z) Q_C  (plus, never a quiet minus).
Q_C already contains gain−loss. Do not put an extra minus on the catalog lobe.
"""

from __future__ import annotations

GENERATOR_SIGN = "+"
GENERATOR = "Q = Q_O + σ(Z) Q_C"
CLAIM = "Model"

_FORBIDDEN = ("toe", "hfb", "mystery", "invariant_hunt")


class _BlockToeManuscript:
    """Fail closed: arena must not import TOE manuscript modules."""

    def find_spec(self, fullname, path=None, target=None):  # noqa: ARG002
        root = fullname.split(".", 1)[0]
        if root in _FORBIDDEN:
            raise ImportError(
                f"arena refuses to import {fullname!r} at runtime. "
                "The mix is a Model, not the TOE manuscript."
            )
        return None


def install_import_guard() -> None:
    import sys

    if any(isinstance(f, _BlockToeManuscript) for f in sys.meta_path):
        return
    sys.meta_path.insert(0, _BlockToeManuscript())


def mix(q_o, sigma, q_c):
    """Software fact: the generator is plus."""
    if GENERATOR_SIGN != "+":
        raise RuntimeError("generator sign flipped; mix is Q_O + σ(Z) Q_C")
    return q_o + sigma * q_c
