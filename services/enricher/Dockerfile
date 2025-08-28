FROM python:3.11-slim-buster

WORKDIR /application

COPY services/enricher/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY services/enricher/app ./services/enricher/app
COPY services/kafka ./services/kafka
COPY services/utiles ./services/utiles

CMD ["python", "-m", "services.enricher.app.main"]