#!/usr/bin/env python3
"""Usar async comprehension para recolectar los 10 números del async_generator"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Recoge los 10 números del async_generator y los devuelve como lista.
    """
    return [num async for num in async_generator()]
