#!/usr/bin/env python3
"""Este módulo define una función que suma una lista con ints y floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Devuelve la suma de una lista con ints y floats como float."""
    return sum(mxd_lst)
