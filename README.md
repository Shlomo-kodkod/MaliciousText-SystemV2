# Malicious Text Detection System V2

Malicious text recognition system microservices with Apache Kafka and MongoDB.

## The system consists of the following services:


### 1. Retriever Service
- A service that returns new tweets from the mongoDB database
 and post the tweets to Kafka by category

### 2. Preprocessor Service  
- Clears and processes the text of the tweets
 Removes punctuation marks, special characters, and stop words
 publishes the processed tweets to Kafka

### 3. Enricher Service
- Adding more information to tweets:
 Sentiment Analysis
 Identifying weapons in the text
 Extracting relevant dates
 Publishing the new tweets to Kafka

### 4. Persister Service
- Keeps the processed  tweets in the database
 separates by catgory

### 5. API Service
- Provides a REST API for data access




### API Endpoints

- antisemitic 

```'http://localhost:8000/antisemitic'```


- not-antisemitic

```'http://localhost:8000/not-antisemitic'```


## Project structure

```
├──data/       # weapons blacklist
├──scripts/    # OS scripts
├──services/
|  ├── api/             # API end points
|  ├── enricher/        # Data enrichment service
|  ├── kafka/           # Kafka service
|  ├── persister/       # Data saving service
|  ├── preprocesor/     # Preprocessing service
|  ├── retriever/       # Data retrieval service
|  └── utiles/
└──README.md
```
