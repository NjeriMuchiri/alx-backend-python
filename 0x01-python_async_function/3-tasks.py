#!/usr/bin/env python3
"""Regular function that takes an int and return asyncio"""
import asyncio


"""Our imported file"""
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """The function that takes an integer and return the async.ioTask"""
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
