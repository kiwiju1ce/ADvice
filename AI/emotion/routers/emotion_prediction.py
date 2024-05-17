from fastapi import APIRouter
from typing import List
from starlette.responses import JSONResponse

from services.emotion_service import EmotionService

emotion = APIRouter()
emotionService = EmotionService()


@emotion.post("/emotion")
def emotion_prediction(data: List[str]):
    return JSONResponse(status_code=200, content=emotionService.predict_all(data))
