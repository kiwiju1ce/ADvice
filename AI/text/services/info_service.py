import logging

from internals.text_analyzer import infoDetector


class InfoService:
    def detail_info_detection(self, texts: tuple[list]) -> tuple[list, list]:
        texts = texts[0]
        logging.info(f'{self.__class__} :  {type(texts)}')
        return infoDetector.detect_texts(texts)


infoService = InfoService()
