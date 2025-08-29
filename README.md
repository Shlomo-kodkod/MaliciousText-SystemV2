# Malicious Text Detection System V2

Malicious text system microservices with Apache Kafka and MongoDB.



### Retriever Service
- Returns tweets from the mongoDB database
 and post the tweets to Kafka by category

### Preprocessor Service  
- Removes punctuation marks, special characters, and stop words
- publishes the processed tweets to Kafka

### Enricher Service
- Sentiment Analysis
- Identifying weapons in the text
- Find relevant dates
- Publishing the new tweets to Kafka

### Persister Service
- Keeps the processed  tweets in the database  separates by catgory


### API Service
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
