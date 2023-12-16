#!/usr/bin/env python3
"""Async comprehension that takes no argument"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """coroutine function that collects 10 random numbers"""
    return [i async for i in async_generator()]


async def main():
    """main function"""
    print(await async_comprehension())

asyncio.run(main())
