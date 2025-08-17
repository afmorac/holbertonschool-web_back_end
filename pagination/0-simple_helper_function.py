#!/usr/bin/env python3
"""
Función de ayuda para paginación
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Devuelve el índice inicial y final según la página y su tamaño
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
