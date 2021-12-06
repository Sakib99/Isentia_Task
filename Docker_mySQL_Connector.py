# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:01:01 2021

@author: user
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  port=80,
  user="python",
  password="sakib",
  database="carles_database"
)
mycursor = mydb.cursor()
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def make_connection():
    mydb = mysql.connector.connect(
            host="localhost",
            port=80,
            connect_timeout=1000,
            user="python",
            password="sakib",
            database="carles_database"
            )
    mycursor = mydb.cursor(prepared=True)
    return mydb,mycursor

def insert_values(mycursor,name,url,category,content,current_time):
    query="""INSERT INTO web_sections_final (wesite_name,wesite_url,category,content,time) 
           VALUES (%s, %s, %s, %s, %s) """
    insert_tuple=(name,url,category,content,current_time)
    try:
        mycursor.execute(query,insert_tuple)
    except:
        print('connection error')
    

def table_create(mycursor):
    mycursor.execute("CREATE TABLE web_sections_final (wesite_name VARCHAR(55),wesite_url VARCHAR(255),category VARCHAR(100),content VARCHAR(3000), time VARCHAR(50))")


#insert_values(mycursor,'l','ll',"ll","ll",current_time)
#sql_select_Query = "select content from web_sections_final where wesite_name=%s and category=%s"
#tup=('9news','sports')
##
#mycursor.execute(sql_select_Query,tup)
#records=mycursor.fetchall()
#print(records)
#mydb.close()
#mycursor.close()