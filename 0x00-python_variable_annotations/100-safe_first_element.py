#!/usr/bin/env python3
"""Duck typing"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a sequence and returns its first element
    if it exists, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
