import os
import sys
import pandas as pd
 
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.utils import read_sql_data


load_dotenv()


@dataclass   #In a normal class, you have to write an __init__ method to assign values. With a dataclass, Python does it automatically.
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

#Automates Path Creation only .doesnt create folder(artifacts) + Prevents "Hardcoding" Errors
# finds folder and ad files in it in some way

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  #It runs automatically when you create an object of the class..obj = DataIngestion()

    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info("Reading completed from MySQL database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=2)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
        
        
        
# ingestion_config here is just an attribute (variable) of your class object that stores a configuration object
# It calls the function you wrote to connect to MySQL using your .env credentials.
#os.path.dirname(...): This looks at the path artifacts/train.csv and extracts just the folder name: artifacts.
#os.makedirs(..., exist_ok=True): This physically creates the artifacts folder on your hard drive. If the folder already exists, it doesn't do anything (it won't crash).
#It takes the entire table from MySQL and saves it as raw.csv inside the artifacts folder.
# It creates two new CSV files in your artifacts folder: train.csv and test.csv.
#You now have three files in your sidebar, ready for the next step of the pipeline.
# return part of the fxn = It "hands over" the paths of the train and test files to whatever code called this function (usually app.py).
# This allows the next component (Data Transformation) to know exactly where to find the data it needs to clean.