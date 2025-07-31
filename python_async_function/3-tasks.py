#!/usr/bin/env python3
"""Este módulo crea una Task (tarea asíncrona) usando wait_random"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crea y devuelve una Task que va a correr la función wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
