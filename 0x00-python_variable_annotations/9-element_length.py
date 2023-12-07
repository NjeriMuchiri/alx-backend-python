#!/usr/bin/env python3
"""Variable annotations that returns tuple from str"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list of strings and
    returns a list of tuples.Each tuple contains a
    string from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
