import logging
from services.enricher.app.manager import Manager

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    manager = Manager()
    manager.run()


if __name__ == '__main__':

    main()  