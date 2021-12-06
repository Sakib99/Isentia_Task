# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 18:03:22 2021

@author: user
"""
import json
from lxml import html
import requests
from Docker_mySQL_Connector import insert_values,make_connection
from datetime import datetime
import time



def time_files_initialize(filename):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    out_file = open(filename, "r") 
    data=json.load(out_file)
    return current_time,data,1

def load_category_contents(mycursor,section,website_name):
        sql_select_Query = "select content,time from web_sections_final where category=%s and wesite_name=%s"
        tuple1 = (section,website_name)
        mycursor.execute(sql_select_Query,tuple1)
        records=mycursor.fetchall()
        contents=[]
        if len(records)>1:
            for i in records:
                contents.append(i[0])
        return contents,e



def get_web_DOM_tree(data,website_name):
    web_url=data[website_name]['url']
    page = requests.get(data[website_name]['url'])
    tree = html.fromstring(page.content)
    return tree,web_url,1


def get_updated_item(latest,contents,web_url,section,website_name,mycursor):
    try:
        for item in latest:
            flag=0
            for value in contents:
                if (item==value):
                    flag=1
            if(flag==0):
                print(web_url+": "+section+" :Updated :"+item)
                insert_values(mycursor,str(website_name),str(data[website_name]['url']),str(section),str(item),current_time)
                mydb.commit()
    except:
        print('error')

def section_scanner(data,website_name,contents,section,web_url,tree,mycursor):
    try:
              latest=tree.xpath(data[website_name][section])
              get_updated_item(latest,contents,web_url,section,website_name,mycursor)
    except:
                   print('')


def web_scanner(mycursor,data):
        for website_name in data:
            tree,web_url,e =get_web_DOM_tree(data,website_name)
            for section in data[website_name]:
                contents,e=load_category_contents(mycursor,section,website_name)
                section_scanner(data,website_name,contents,section,web_url,tree,mycursor)
                #insert_values(mycursor,str(website_name),str(data[website_name]['url']),str(section),str(item),current_time)
                
        return 1
if __name__ == "__main__":  
    while(True):
        print('hello geek!')
        time.sleep(300)
        current_time,data,e=time_files_initialize("my_web_Xpath1.json")  
        mydb,mycursor=make_connection()                   
        web_scanner(mycursor,data)
        print('hey')
        #mydb.close()
        mycursor.close()
