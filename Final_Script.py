# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:03:22 2021

@author: user
"""
import json
from lxml import html
import requests





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

def insert_values(mycursor,name,url,category,content,current_time):
    query="""INSERT INTO web_sections_test1 (wesite_name,wesite_url,category,content,time) 
           VALUES (%s, %s, %s, %s, %s) """
    insert_tuple=(name,url,category,content,current_time)
    mycursor.execute(query,insert_tuple)
    sql_select_Query = "select * from web_sections_test1"

    mycursor.execute(sql_select_Query)
    
    records=mycursor.fetchall()
    print(records)
def table_create(mycursor):
    mycursor.execute("CREATE TABLE web_sections_test1 (wesite_name VARCHAR(55),wesite_url VARCHAR(255),category VARCHAR(100),content VARCHAR(3000), time VARCHAR(50))")




out_file = open("my_web_Xpath1.json", "r") 
    
data=json.load(out_file) 
for website_name in data:
    
    page = requests.get(data[website_name]['url'])
    tree = html.fromstring(page.content)
    for section in data[website_name]:
        print(section)
        try:
           
        #This will create a list of buyers:
            try:
              latest=tree.xpath(data[website_name][section])
              for item in latest:
                  #print(mycursor,website_name,data[website_name]['url'],section,item,current_time)
                  insert_values(mycursor,str(website_name),str(data[website_name]['url']),str(section),str(item),current_time)
              print("")
            except:
              print('')
        except:
            print('')
mydb.commit()
mydb.close()
    
