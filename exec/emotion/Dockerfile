FROM python:3.7.9
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY .. .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

