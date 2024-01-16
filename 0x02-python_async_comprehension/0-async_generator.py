#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
"""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator coroutine that yields random numbers.

    Args:
        float: A random float number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
