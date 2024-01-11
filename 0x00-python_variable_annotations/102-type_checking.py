#!/usr/bin/env python3
"""
mypy to validate the following piece of code
"""

from typing import Tuple, List, TypeVar

T = TypeVar('T')


def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> List[T]:
    zoomed_in: List[T] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x: List[int] = zoom_array(tuple(array))

zoom_3x: List[int] = zoom_array(tuple(array), 3)
