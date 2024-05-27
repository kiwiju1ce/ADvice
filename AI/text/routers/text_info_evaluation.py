from fastapi import APIRouter
from typing import List
from starlette.responses import JSONResponse

from models.detail_request import DetailRequest
from models.exception.custom_exception import CustomException
from services.info_service import infoService
from services.process_executor import process_executor

info = APIRouter()


@info.post("/info-evaluate")
async def text_info_evaluate(data: List[str]):
    if not data:
        raise CustomException(422, "No texts provided")

    result = await process_executor(infoService.detail_info_detection, data)
    preds, scores = result
    return JSONResponse(status_code=200, content=DetailRequest(prediction=preds, score=scores).dict())
