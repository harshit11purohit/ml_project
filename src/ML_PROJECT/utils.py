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
    
    
# pymysql: This is the "driver." Think of it as the specialized cable that allows Python to plug into a MySQL database.
#It knocks on the door of your MySQL server at localhost:3306.
#: It provides the credentials from your .env. If the password is correct, MySQL opens a "session" or "tunnel" for data to flow through.

#This is the magic line. It sends the SQL command SELECT * FROM student through the tunnel.

#CustomException
# What it does: If the database is off, or the password is wrong, this "catches" the crash.

#Why: Instead of showing a messy, confusing error, it uses your custom script to tell you exactly which file and line caused the problem (like we saw earlier with the "Access Denied" error).