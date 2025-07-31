#!/usr/bin/env python3
"""Este módulo lanza varias coroutines al mismo tiempo y devuelve los resultados en orden"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Corre wait_random n veces en paralelo con el mismo max_delay
    Devuelve los tiempos en orden (de menor a mayor), sin usar sort()
    """
    tasks = []  # aquí guardamos las tareas
    delays = []  # aquí vamos a guardar los resultados (floats)

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))  # lanzamos cada tarea

    for task in asyncio.as_completed(tasks):  # esta parte espera según van terminando
        result = await task
        delays.append(result)  # vamos guardando los resultados en el orden que terminan

    return delays
