# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:34:09 2018

@author: fmdu
"""

import mysql 

db=_mysql.connect()

db=_mysql.connect(host="localhost",user="chnordfr_zenc402", passwd="Ezwof01d!",db="chnord_python")

db.query("""SELECT * FROM `test` WHERE 1""")

r=db.store_result()

print(r)