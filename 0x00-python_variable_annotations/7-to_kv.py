#!/usr/bin/env python3
"""Returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string and an int plus float
      and returns a tuple"""
    return (k, v**2.0)
