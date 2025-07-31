#!/usr/bin/env python3
"""Este módulo lanza varias tareas con task_wait_random y devuelve los delays en orden"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Corre task_wait_random n veces en paralelo con el mismo max_delay
    Devuelve los tiempos en orden (de menor a mayor), sin usar sort()
    """
    tasks = []  # aquí guardamos las tareas
    delays = []  # aquí vamos a guardar los resultados (floats)

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))  # usamos la función que devuelve un task

    for task in asyncio.as_completed(tasks):  # se resuelven en orden según terminan
        result = await task
        delays.append(result)

    return delays
