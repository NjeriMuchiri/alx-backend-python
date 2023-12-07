#!/usr/bin/env python3
"""Sum of mixed data types"""
from typing import List, Union


def sum_mixed_list(mxd__lst: List[Union[int, float]]) -> float:
    """This method adds int and floats and returns the sum in float"""
    return sum(mxd__lst)
