#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as arguments
"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Asynchronous coroutine that measures the total execution
    time for wait_n(n, max_delay), and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay.

    Returns:
        float: Total execution time for wait_n(n, max_delay) divided by n.
    """
    start_time = asyncio.get_running_loop().time()
    await wait_n(n, max_delay)
    end_time = asyncio.get_running_loop().time()
    return (end_time - start_time) / n
