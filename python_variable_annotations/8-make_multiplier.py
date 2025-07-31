#!/usr/bin/env python3
"""Este módulo define una función que genera multiplicadores."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Devuelve una función que multiplica por `multiplier`."""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
