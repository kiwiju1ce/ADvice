import sys

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    max_workers: int
    ad_detection_model_path: str
    info_detection_model_path: str
    yolo_model_path: str
    pretrained_electra_tokenizer: str
    pretrained_kobert_tokenizer: str
    user_agent: str

    class Config:
        env_file = ".env"


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
settings = Settings()
