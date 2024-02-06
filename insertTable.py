# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 21:16:11 2023

@author: sijian
"""

import pyodbc
import pandas as pd
# import os

value1 = input('Please input date in yyyy-mm-dd....\n')
value2 = input('Please input gasoline volume....\n')
value3 = input('Please input money spent....\n')
value4 = input('Please input Kilometers run if possible....\n')

if value4 == '':
	value4 = 'NULL'

# set up SQL server settings
SERVER = 'localhost'
DATABASE = 'sijian'

if value4 == 'NULL':
    sql_query =  """
    insert into [sijian].[dbo].[GasRecord]
    values ('{}','{}','{}',NULL)
    """.format(value1,value2,value3)
else:
    sql_query =  """insert into [sijian].[dbo].[GasRecord] values ('{}','{}','{}','{}')""".format(value1,value2,value3,value4)
# sql_query = "select * from [dbo].[gasrecord]"

print(sql_query)

connectionString = r"DRIVER={ODBC Driver 17 for SQL Server};SERVER=sijian;DATABASE={sijian};Trusted_Connection=yes;"
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute(sql_query)
conn.commit()

print("insert successfully")
