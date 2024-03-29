#!/usr/bin/env python3
"""
type-annotated function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of int/float v."""
    return k, v ** 2
