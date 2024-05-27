from fastapi import APIRouter
from typing import List
from starlette.responses import JSONResponse

from models.detail_request import DetailRequest
from models.exception.custom_exception import CustomException
from services.ad_service import adService
from services.process_executor import process_executor

text = APIRouter()


@text.post("/ad-evaluate")
async def text_ad_evaluate(data: List[str]):
    if not data:
        raise CustomException(422, "No texts provided")

    preds, scores = await process_executor(adService.ad_evaluation, data)
    return JSONResponse(status_code=200, content=DetailRequest(prediction=preds, score=scores).dict())


@text.post("/ad-evaluate/short")
async def text_ad_evaluate(data: List[str], path: List[str]):
    if not data:
        raise CustomException(422, "No texts provided")
    return JSONResponse(status_code=200,
                        content=await process_executor(
                            adService.ad_evaluation_shortcut, data, path
                        ))
