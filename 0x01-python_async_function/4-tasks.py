#!/usr/bin/env python3
"""
task_wait_n
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in 2 int arguments (in this order):
    n and max_delay. It spawns task_wait_random n times with the
    specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay.

    Returns:
        List[float]: List of all the delays (float values).
        The list of the delays is in ascending order without
        using sort() because of concurrency.
    """
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
