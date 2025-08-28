FROM python:3.11-slim

WORKDIR /app

COPY services/preprocesor/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet

COPY services/preprocesor/app ./services/preprocesor/app
COPY services/kafka ./services/kafka
COPY services/utiles/cleaner.py ./services/utiles/cleaner.py

CMD ["python", "-m", "services.preprocesor.app.main"]