#!/usr/bin/env python3
""" a python module to measure the execution time"""
import time
import async
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtine() -> float:
    """
    measure_runtime - function executiojn async_com 4 times
    Arguments:
        nothing
    Return:
        the total execution time required to complete the task
    
    """
    t_start = time.perf_counter()
    tast = [async_comprehension(0 for i in range(4)]
            await asyncio.gather(*task)
            t_end = time.perf_counter()
            return (t_end - t_start)

