FROM python:3.11-slim

WORKDIR /app

COPY services/retriever/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY services/retriever/app ./services/retriever/app
COPY services/kafka ./services/kafka
COPY services/utils/dal.py ./services/utils/dal.py

CMD ["python", "-m", "services.retriever.app.main"]