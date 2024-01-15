#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at
the same time with async"""

import asyncio
import random
from typing import List
import itertools as it

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays (float values)
    generated from wait_random"""
    resp = await asyncio.gather(*(it.repeat(wait_random(max_delay), n)))
    return list(resp)
