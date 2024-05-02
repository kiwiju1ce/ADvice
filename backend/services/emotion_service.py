from functools import reduce

from models.detail_request import DetailRequest
from internals.emotion_prediction import EmoPrediction


class EmotionPredictionService:
    def __init__(self):
        self.__emotion_prediction = EmoPrediction()

    async def predict(self, data: DetailRequest):
        data = [
            {"id": tag.id, "data": tag.data.replace("\u200B", ""), "type": tag.type}
            for tag in data.script
        ]
        return {"emoPrediction": await self.predict_emo(data)}

    async def predict_emo(self, data):
        text = list(filter(lambda tag: tag["type"] == "txt", data))

        if len(text) < 1:
            return {}

        paragraph = "".join(reduce(lambda x, y: x + y, map(lambda x: x["data"], text)))
        result = self.__emotion_prediction.cnt_emo(paragraph)

        return self.emotion_analyze(result[0], result[1], result[2])

    # 감정값 기반 글 성향 분석 결과 반환
    def emotion_analyze(self, cnt_neg, cnt_neu, cnt_pos):
        # 부정/중립/긍정 중 가장 높은 비율을 가지는 것 반환
        result = 0
        if cnt_neg >= cnt_neu + cnt_pos:
            result = -1
        elif cnt_pos >= cnt_neg + cnt_neu:
            result = 1
        return result