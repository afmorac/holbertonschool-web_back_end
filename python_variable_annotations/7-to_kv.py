#!/usr/bin/env python3
"""Este módulo define una función que devuelve un string y el cuadrado de un número."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Devuelve un tuple con el string y el cuadrado de v como float."""
    return (k, float(v ** 2))
