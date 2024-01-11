#!/usr/bin/env python3
"""
duck-typed annotations
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[None]]:
    """Return the first element of the sequence if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
