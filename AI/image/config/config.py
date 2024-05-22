import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    max_workers: int
    fasttext_model_path: str
    yolo_model_path: str
    target_language_code: str
    google_application_credentials: str

    class Config:
        env_file = ".env"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./model/google/sound-catalyst-421203-3bf1190b292d.json"
settings = Settings()
