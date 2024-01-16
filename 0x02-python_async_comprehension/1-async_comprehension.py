#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that uses async comprehension to
    collect 10 random numbers.

    Returns:
        List[float]: A list containing 10 random float numbers.
    """
    return [i async for i in async_generator()]
