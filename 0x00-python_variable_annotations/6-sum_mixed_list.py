#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of integers and floats in the mixed list."""
    return sum(mxd_lst)
