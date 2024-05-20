FROM python:3.10
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .
ENV GOOGLE_APPLICATION_CREDENTIALS="./model/google/sound-catalyst-421203-3bf1190b292d.json"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]