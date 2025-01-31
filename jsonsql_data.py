import pandas as pd

df = pd.read_json('train.json')

print(df)

"""WORKING WITH JSON_API"""

pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')

"""WITH SQL acts a bridge between python and sql database to communicate"""

!pip install mysql.connector

import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')

df = pd.read_sql_query("SELECT * FROM countrylanguage",conn)

df
