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

if value4 == 'NULL':
    sql_query =  """insert into [sijian].[dbo].[GasRecord] values ('{}','{}','{}',NULL) """.format(value1,value2,value3)
else:
    sql_query =  """insert into [sijian].[dbo].[GasRecord] values ('{}','{}','{}','{}')""".format(value1,value2,value3,value4)
# sql_query = "select * from [dbo].[gasrecord]"

# sql_query = "select * from [dbo].[GasRecord] order by Date"

print(sql_query)


connectionString = r'Driver={ODBC Driver 17 for SQL Server};Server={sijian-laptop};Database={sijian};UID=SA;PWD=Mjrr7788!;Trusted_Connection=no;'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute(sql_query)
conn.commit()

# print(pd.DataFrame.from_records(cursor.fetchall(), columns = [i[0] for i in cursor.description]))

print("insert successfully")
