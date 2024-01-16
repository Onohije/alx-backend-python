#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""

import asyncio
import itertools as it
import time

async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    s = time.perf_counter()
    await asyncio.gather(*list(it.repeat(async_c(), 4)))
    return (time.perf_counter() - s)
