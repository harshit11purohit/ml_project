import os
import pymysql
import sys
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.logger import logging
from dataclasses import dataclass
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("reading sql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=3306
        )
        logging.info("connection established:{mydb}")
        df=pd.read_sql_query('select * from student',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex,sys)
    