#!/usr/bin/env python3
"""
Paginación con metadatos (hypermedia)
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Devuelve datos y metadatos de la paginación
        """
        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(
            total_items / page_size
        )

        current_size = len(data_page)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": current_size,
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
