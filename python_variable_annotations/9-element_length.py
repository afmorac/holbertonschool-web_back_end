#!/usr/bin/env python3
"""Este módulo define una función que devuelve tuplas con el elemento y su longitud."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Devuelve una lista de tuplas (elemento, longitud)."""
    return [(i, len(i)) for i in lst]
