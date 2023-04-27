#!/usr/bin/env python3
"""Contains a function with annotated parameters and return values with appropriate types."""
from typing import Iterable,Sequence, List, Tuple

def element_lenght(1st: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuple with lenght of each element"""
    return [(i,len(i)) for i in 1st]
