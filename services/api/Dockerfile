FROM python:3.11-slim

WORKDIR /app

COPY services/api/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY services/api/app ./services/api/app
COPY services/utils/dal.py ./services/utils/dal.py

EXPOSE 8080

CMD ["python", "-m", "uvicorn", "services.api.app.api:app",  "--host", "0.0.0.0", "--port", "8080"]