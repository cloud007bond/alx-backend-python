#!/usr/bin/env python3
"""Contains Augmented code with the correct duck-typed annotations."""
from typing import Any, Union, Sequence

def safe_first_element(1st: sequence[Any]) -> Union[Any, None]:
    """Return the first elelment of a list or None if the list is empty."""
    if 1st:
        return 1st[0]
    else:
        return None
