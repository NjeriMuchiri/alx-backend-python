#!/usr/bin/env python3
"""Async generator method"""
import asyncio
import random


async def async_generator():
    """function that yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def print_yielded_values():
    """function that stores the result in a list"""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
