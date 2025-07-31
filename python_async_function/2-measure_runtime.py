#!/usr/bin/env python3
"""Este módulo mide cuánto tiempo tarda en promedio correr wait_n"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Corre wait_n(n, max_delay) y mide el tiempo total que tarda.
    Devuelve el promedio dividiendo ese tiempo entre n.
    """
    start = time.perf_counter()  # marcamos la hora de inicio
    asyncio.run(wait_n(n, max_delay))  # corremos la función asíncrona
    end = time.perf_counter()  # marcamos la hora de final

    total_time = end - start  # cuánto se tardó en total
    return total_time / n  # promedio por cada coroutine
