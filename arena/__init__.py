"""Arena: ranked roles + incompleteness dynamics + Alignment that must be corrected."""

from .generator import GENERATOR, GENERATOR_SIGN, install_import_guard, mix
from .state import World

install_import_guard()

__version__ = "0.1.0"
__all__ = ["GENERATOR", "GENERATOR_SIGN", "World", "__version__", "mix"]
