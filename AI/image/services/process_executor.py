import asyncio
import logging
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

from config.config import settings
from models.exception.custom_exception import CustomException

mp.set_start_method('spawn', force=True)
executor = ProcessPoolExecutor(max_workers=settings.max_workers)


async def process_executor(task, *args):
    loop = asyncio.get_running_loop()
    try:
        result = await loop.run_in_executor(executor, task, args)
        return result
    except Exception as e:
        logging.error(f"run_in_executor: {e}")
        raise CustomException(500, "서버에 치명적 오류가 발생했습니다.")
