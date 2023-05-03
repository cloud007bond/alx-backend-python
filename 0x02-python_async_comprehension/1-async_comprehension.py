#!/usr/bin/env python3
""" a python module to return numbers async comprehension"""
from typing import list
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[float]:
    """
    async_comprehension- function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt
