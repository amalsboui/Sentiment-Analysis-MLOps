FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .
COPY models ./models


EXPOSE 8088

CMD ["uvicorn", "FastAPI.app:app", "--host", "0.0.0.0", "--port", "8088"]

