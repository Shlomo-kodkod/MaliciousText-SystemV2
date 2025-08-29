FROM python:3.11-slim

WORKDIR /app

COPY services/preprocessor/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet

COPY services/preprocessor/app ./services/preprocessor/app
COPY services/kafka ./services/kafka
COPY services/utils/cleaner.py ./services/utils/cleaner.py

CMD ["python", "-m", "services.preprocessor.app.main"]