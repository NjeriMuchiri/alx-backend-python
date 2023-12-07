#!/usr/bin/env python3
"""Multiplier variable annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that takes a float multiplier and returns a float multipier"""
    def multiplierFunction(x: float) -> float:
        return x * multiplier
    return multiplierFunction
