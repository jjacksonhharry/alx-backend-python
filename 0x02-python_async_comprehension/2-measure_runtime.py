#!/usr/bin/env python3
"""
coroutine that will execute async_comprehension
"""
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
