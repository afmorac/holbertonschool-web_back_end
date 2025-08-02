#!/usr/bin/env python3
"""Este módulo genera números aleatorios de forma asíncrona"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Esta función corre 10 veces, espera 1 segundo en cada vuelta,
    y devuelve un número aleatorio entre 0 y 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # espera 1 segundo sin trancar el programa
        yield random.uniform(0, 10)  # devuelve un número random entre 0 y 10
