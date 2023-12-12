#!/usr/bin/env python3
"""This function measures the total execution time """
import asyncio
import time


"""The imported file"""
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Function with int that measures the total execution
    time for wait_n and returns total_time"""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(asyncio.run(measure_time(n, max_delay)))
