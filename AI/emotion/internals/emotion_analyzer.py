import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List


class EmotionPrediction:
    # 초기화
    def __init__(self):
        self.device = torch.device('cpu')
        self.model = (AutoModelForSequenceClassification.from_pretrained("./model/emotion_classification", num_labels=3)
                      .to(self.device))
        self.tokenizer = AutoTokenizer.from_pretrained("monologg/distilkobert")

    # 예측
    def detect(self, texts: List[str]) -> List[int]:
        types = []

        self.model.eval()
        for text in texts:
            types.append(self.__DistilKoBERT(text))

        return types

    def __DistilKoBERT(self, text) -> int:
        tokenized_text = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            add_special_tokens=True,
            max_length=128
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(
                input_ids=tokenized_text["input_ids"],
                attention_mask=tokenized_text["attention_mask"]
            )

        logits = outputs[0].detach().cpu()
        print(logits)
        return int(logits.argmax(-1))


emotionPrediction = EmotionPrediction()
print(emotionPrediction.detect([
    "편하고 좋긴 한데 혹 자주 빨으면 허리가 늘어난거 같음 그래도 현재는 좋아요 ~"]))
