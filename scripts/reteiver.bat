docker build -f services/retriever/Dockerfile -t kodkod1docker/retriever:v1.0 .

docker run --name retriever -d --network text-analyzer kodkod1docker/retriever:v1.0

docker build -f services/preprocesor/Dockerfile -t kodkod1docker/preprocesor:v1.0 .

docker run --name preprocesor -d --network text-analyzer kodkod1docker/preprocesor:v1.0

docker build -f services/enricher/Dockerfile -t kodkod1docker/enricher:v1.0 .

docker run --name enricher -d --network text-analyzer kodkod1docker/enricher:v1.0

docker build -f services/persister/Dockerfile -t kodkod1docker/persister:v1.0 .

docker run --name persister -d --network text-analyzer kodkod1docker/persister:v1.0


docker build -f services/api/Dockerfile -t kodkod1docker/dataretrieval:v1.0 .

docker run --name dataretrieval -d -p 8080:8080 --network text-analyzer kodkod1docker/dataretrieval:v1.0


