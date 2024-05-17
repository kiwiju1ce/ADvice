from typing import List, Tuple
from models.exception.custom_exception import CustomException
from internals.emotion_analyzer import emotionPrediction


class EmotionService:
    # 데이터 전처리 이후 감정 예측 수행
    def predict_all(self, data: List[str]):
        # 전처리
        texts = [
            text.replace("\u200B", "")
            for text in data
        ]

        # 예측 시작
        results = _predict(texts)

        # 반환
        keys = ["negative", "neutral", "positive"]
        return dict(zip(keys, results))


def _predict(texts) -> List[List[str]]:
    pos_list, neu_list, neg_list = [], [], []
    types = emotionPrediction.detect(texts)

    for type, text in zip(types, texts):
        if type == 0:
            neg_list.append([text, type])
        elif type == 1:
            neu_list.append([text, type])
        elif type == 2:
            pos_list.append([text, type])
        else:
            raise CustomException(400, "잘못된 모델 설정")

    pos_list = [data[0] for data in sorted(pos_list, key=lambda d: d[1], reverse=True)]
    neu_list = [data[0] for data in sorted(neu_list, key=lambda d: d[1], reverse=True)]
    neg_list = [data[0] for data in sorted(neg_list, key=lambda d: d[1], reverse=True)]

    return [neg_list, neu_list, pos_list]


emotionService = EmotionService()
