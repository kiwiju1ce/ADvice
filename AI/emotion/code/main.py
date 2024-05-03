from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from emotion.code.routers.emotion_prediction import emotion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(emotion)