#!/usr/bin/env python3
"""
Paginación hypermedia tolerante a borrados
"""

import csv
import math
from typing import List, Dict


class Server:
    """Servidor para paginar la base de nombres"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cache del dataset (sin el header)"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexado por posición (comienza en 0)"""
        if self.__indexed_dataset is None:
            data = self.dataset()
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Devuelve página y metadatos, saltando índices borrados
        """
        if index is None:
            index = 0

        # Validaciones
        assert isinstance(index, int) and isinstance(page_size, int)
        assert page_size > 0

        idx_data = self.indexed_dataset()
        max_len = len(idx_data)
        assert 0 <= index < max_len

        data: List[List] = []
        cursor = index

        # Recolecta 'page_size' ítems existentes,
        # saltando huecos por borrados
        while len(data) < page_size and cursor < max_len:
            if cursor in idx_data:
                data.append(idx_data[cursor])
            cursor += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": cursor
        }
