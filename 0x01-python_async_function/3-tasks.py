#!/usr/bin/env python3
"""3. Tasks 3. Tasks 3. Tasks"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
