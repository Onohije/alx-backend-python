#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Wait 1 second, then yield a random number
    between 0 and 10, 10 times"""
    arr = []
    for _ in range(10):
        arr.append(random.uniform(0, 10))
    for i in arr:
        await asyncio.sleep(1)
        yield i
