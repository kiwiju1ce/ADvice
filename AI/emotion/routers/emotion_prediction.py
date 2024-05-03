from fastapi import APIRouter
from starlette.responses import JSONResponse

from models.emotion_request import EmotionRequest
from services.emotion_service import EmotionPredictionService

emotion = APIRouter(prefix="/emo-predict")
emotionService = EmotionPredictionService()


@emotion.post("")
async def emotion_prediction(data: EmotionRequest):
    return JSONResponse(status_code=200, content=await emotionService.predict(data))
