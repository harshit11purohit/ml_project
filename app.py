from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
# from src.ML_project import logger
from src.ML_PROJECT.components.data_ingestion import DataIngestion
from src.ML_PROJECT.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info(" the execution has started")
    
    try:
       data_ingestion=DataIngestion()
       data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info(" custom exception")
        raise CustomException(e,sys)


