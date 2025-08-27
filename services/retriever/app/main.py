import logging
from services.retriever.app.retriever import Retrieval


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler()])



def main():
    retriever = Retrieval()
    retriever.run()

if __name__ == "__main__":
    main()  