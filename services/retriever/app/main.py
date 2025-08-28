import logging
from services.retriever.app.retriever import Retrieval

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)



def main():
    retriever = Retrieval()
    retriever.run()

if __name__ == "__main__":
    main()  