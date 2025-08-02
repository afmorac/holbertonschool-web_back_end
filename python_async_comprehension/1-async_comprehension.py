#!/usr/bin/env python3
"""Recolecta 10 números usando async comprehension."""

from typing import List


async def async_comprehension() -> List[float]:
    """
    Recoge los 10 números del async_generator y los devuelve como lista.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [num async for num in async_generator()]