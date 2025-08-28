import logging
from services.enricher.app.manager import Manager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', handlers=[logging.StreamHandler()])

def main():
    manager = Manager()
    manager.run()


if __name__ == '__main__':

    main()