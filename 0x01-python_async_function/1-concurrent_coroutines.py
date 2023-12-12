#!/usr/bin/env python3
"""Async routine that takes in 2 int arguments"""
import asyncio
from typing import List


"""Importing our previous file"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """This is our async method that takes two arguments"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)

if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
