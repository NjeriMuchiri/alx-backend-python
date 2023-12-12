#!/usr/bin/env python3
"""This is an asynchronos coroutine that takes an integer"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This is the method for async"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))