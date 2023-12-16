#!/usr/bin/env python3
"""measuring runtime coroutine that executes
asynccomprehension four times"""
import asyncio


"""our imports"""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """fucntion that measures the total runtime and return it"""
    start_time = asyncio.get_event_loop().time()

    """Execute async_comprehension four times in parallel
    using asyncio.gather"""
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
