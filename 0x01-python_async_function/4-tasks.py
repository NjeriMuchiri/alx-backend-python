#!/usr/bin/env python3
"""Takes the code from wait_n and alter it in a new function"""
import asyncio
from typing import List


"""The imported file"""
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Our function that alters into a new func"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
