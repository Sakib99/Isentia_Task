# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:36:18 2021

@author: user
"""
import time,datetime
import unittest
import time
from Docker_mySQL_Connector import make_connection
from Final_Script import *
class TestScript(unittest.TestCase):
    def test_script_files_config(self):
        
        s,d,e=time_files_initialize("my_web_Xpath1.json")
        val=(s,d,e)
        print(self.assertAlmostEqual(e,1,'yes'))
        
    
    def test_scanner(self):
         s,d,e=time_files_initialize("my_web_Xpath1.json")      
         mydb,mycursor=make_connection()
         K=web_scanner(mycursor,d)
         print(self.assertAlmostEqual(K,1,'yes'))
    def load_DOM_tree(self):
       s,d,e=time_files_initialize("my_web_Xpath1.json")  
       a,b,e=get_web_DOM_tree(d,'7news')
       print(e)
       print(self.assertAlmostEqual(e,1,'yes'))
    def load_content(self):
       mydb,mycursor=make_connection()
       b,e=load_category_contents(mycursor,'sport','9news')
       print(self.assertAlmostEqual(e,1,'yes'))
       
if __name__ == '__main__':
    unittest.main()
       
       
