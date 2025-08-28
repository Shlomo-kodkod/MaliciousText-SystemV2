from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import logging
from services.dal import DAL
from services.api.app import config


app = FastAPI()
dal = DAL(config.uri)
logger = logging.getLogger(__name__)

@app.get("/antisemitic")
def get_antisemitic():
    """
    Endpoint to retrieve antisemitic from the database.
    Returns the data or an error message if the retrieval fails.
    """
    try:
        dal.connect()
        data = dal.read_collection(config.collection_antisemitic)
        logger.info("Data received successfully")
        return JSONResponse(content=data)
    except Exception as e:
        logger.error("Error while receiving data")
        return JSONResponse(content={"Error": e})
    
@app.get("/not-antisemitic")
def get_antisemitic():
    """
    Endpoint to retrieve not antisemitic from the database.
    Returns the data or an error message if the retrieval fails.
    """
    try:
        dal.connect()
        data = dal.read_collection(config.collection_not_antisemitic)
        logger.info("Data received successfully")
        dal.disconnect()
        return JSONResponse(content=data)
    except Exception as e:
        logger.error("Error while receiving data")
        return JSONResponse(content={"Error": e})
    

        