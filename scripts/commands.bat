docker build -f services/retriever/Dockerfile -t kodkod1docker/retriever:v1.0 .

docker build -f services/preprocesor/Dockerfile -t kodkod1docker/preprocesor:v1.0 .

docker build -f services/enricher/Dockerfile -t kodkod1docker/enricher:v1.0 .

docker build -f services/persister/Dockerfile -t kodkod1docker/persister:v1.0 .

docker build -f services/api/Dockerfile -t kodkod1docker/dataretrieval:v1.0 .



docker network create text-analyzer


docker run -d  
  --name broker 
  --network text-analyzer
  -e KAFKA_NODE_ID=1 
  -e KAFKA_PROCESS_ROLES=broker,controller 
  -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092 
  -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER 
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT 
  -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@broker:9093 
  -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 
  -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 
  -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 
  -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 
  -e KAFKA_NUM_PARTITIONS=3 
  -e KAFKA_AUTO_CREATE_TOPICS_ENABLE=true
  apache/kafka:latest

docker run -d 
  --name mongodb-community-server
  --network text-analyzer
  mongodb/mongodb-community-server:latest


docker run --name retriever -d --network text-analyzer kodkod1docker/retriever:v1.0

docker run --name preprocesor -d --network text-analyzer kodkod1docker/preprocesor:v1.0

docker run --name enricher -d --network text-analyzer kodkod1docker/enricher:v1.0

docker run --name persister -d --network text-analyzer kodkod1docker/persister:v1.0

docker run --name dataretrieval -d -p 8080:8080 --network text-analyzer kodkod1docker/dataretrieval:v1.0