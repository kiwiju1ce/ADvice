import asyncio
from concurrent.futures import ProcessPoolExecutor

from config.config import settings

executor = ProcessPoolExecutor(max_workers=settings.max_workers)


async def process_executor(task, *args):
    loop = asyncio.get_running_loop()
    print(task)
    result = await loop.run_in_executor(executor, task, args)
    return result
