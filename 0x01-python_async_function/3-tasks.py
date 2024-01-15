#!/usr/bin/env python3
"""
task_wait_random that takes an integer max_delay and
returns a asyncio.Task
"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int): Maximum delay.

    Returns:
        asyncio.Task: A task that waits for a random delay between 0 and
        max_delay (included and float value) seconds and eventually returns it.
    """
    return asyncio.create_task(wait_random(max_delay))
