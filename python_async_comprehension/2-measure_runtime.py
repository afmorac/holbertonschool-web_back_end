#!/usr/bin/env python3
"""Mide el tiempo que tardan 4 async_comprehensions corriendo en paralelo"""

import asyncio
import time


async def measure_runtime() -> float:
    """
    Ejecuta async_comprehension 4 veces en paralelo y devuelve el tiempo total.
    """
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
