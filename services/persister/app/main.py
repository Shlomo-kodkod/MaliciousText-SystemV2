import logging
from services.persister.app.persister import Persister


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



def main():
    persister = Persister()
    persister.run()

if __name__ == "__main__":
    main()