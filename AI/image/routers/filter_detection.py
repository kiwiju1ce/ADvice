from typing import List

from fastapi import APIRouter
from starlette.responses import JSONResponse

from models.exception.custom_exception import CustomException
from services.image_detection_service import imageService
from services.process_executor import process_executor

filter_detect = APIRouter(prefix="/filter-detection")


@filter_detect.post("")
async def filter_evaluation(data: List[str]):
    if not data:
        raise CustomException(422, "image_path is empty")
    return JSONResponse(status_code=200,
                        content=await process_executor(
                            imageService.filter_detection, data
                        ))
