#!/usr/bin/env python3
"""
Paginación simple sobre un CSV de nombres
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Devuelve (inicio, fin) para la página dada
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Servidor para paginar el dataset de nombres de bebés"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cache del dataset (sin el header)"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Devuelve las filas de la página solicitada
        """
        # Validaciones
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        # Fuera de rango → lista vacía
        if start >= len(data):
            return []

        return data[start:end]
