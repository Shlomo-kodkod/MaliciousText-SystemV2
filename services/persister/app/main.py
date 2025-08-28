import logging
from services.persister.app.presister import Presister


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler()])


def main():
    persister = Presister()
    persister.run()

if __name__ == "__main__":
    main()