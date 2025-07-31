#!/usr/bin/env python3
"""Este módulo tiene una función que espera un tiempo aleatorio (usando asyncio y random)"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Esta función espera un tiempo aleatorio entre 0 y max_delay (puede ser decimal)
    y luego devuelve ese número. El delay se hace de forma asíncrona.
    """
    delay = random.uniform(0, max_delay)  # aquí cogemos un número decimal aleatorio
    await asyncio.sleep(delay)  # esperamos ese tiempo sin frizar el programa
    return delay  # devolvemos ese delay que usamos
