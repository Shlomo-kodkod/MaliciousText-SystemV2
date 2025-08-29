FROM python:3.11-slim

WORKDIR /app

COPY services/persister/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY services/persister/app ./services/persister/app
COPY services/kafka ./services/kafka
COPY services/utils/dal.py ./services/utils/dal.py

CMD ["python", "-m", "services.persister.app.main"]