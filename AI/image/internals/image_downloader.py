from typing import Tuple

import cv2
import urllib.request
import urllib.error
import numpy as np
from PIL import Image
from io import BytesIO

from models.exception.custom_exception import CustomException


class ImageDownloader:
    def load_image_from_url(self, url: str) -> np.ndarray:
        try:
            response = urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            raise CustomException(400, "이미지 로드 중 문제가 발생했습니다")

        image = np.asarray(bytearray(response.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        return image

    def _get_image_resolution(self, image: np.ndarray) -> Tuple[int, int]:
        image = Image.open(BytesIO(image))
        width, height = image.size
        return width, height


downloader = ImageDownloader()