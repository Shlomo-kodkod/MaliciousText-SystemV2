import logging
from services.persister.app.presister import Presister


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def main():
    persister = Presister()
    persister.run()

if __name__ == "__main__":
    main()