from internals.text_analyzer import infoDetector


class InfoService:
    def detail_info_detection(self, texts: tuple[list]) -> tuple[list, list]:
        texts = texts[0]
        return infoDetector.detect_texts(texts)


infoService = InfoService()
