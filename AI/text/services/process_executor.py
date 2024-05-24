import asyncio
from concurrent.futures import ProcessPoolExecutor

from config.config import settings

executor = ProcessPoolExecutor(max_workers=settings.max_workers)


async def process_executor(task, *args):
    # future = executor.submit(task, args)
    # try:
    #     result = asyncio.wrap_future(future)
    #     print(f"Result: {result}")
    # except asyncio.TimeoutError:
    #     print("Task timed out")
    # except Exception as e:
    #     print(f"Error in executor.submit: {e}")
    loop = asyncio.get_running_loop()
    print(loop.is_running())
    loop.set_debug(True)
    print(task)
    try:
        result = await loop.run_in_executor(executor, task, args)
        return result
    except Exception as e:
        print(f"Error in run_in_executor: {e}")
