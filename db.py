# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:34:09 2018

@author: fmdu
"""

import _mysql
import os

############ ouverture de fichier et lecture

with open('data_test.txt', 'r') as mon_fichier:
    texte = mon_fichier.readlines()
    for ligne in texte :
        words = ligne.split(";")
    
    for i in range(0,len(words)-1):
        print words[i]
 


############ gestion de la base de données mysql : écriture du fichier en base



db=_mysql.connect(host="localhost",user="chnordfr_mike", passwd="Ezwof01d!",db="chnordfr_python")

db.query("""SELECT * FROM `test` WHERE 1""")

r=db.store_result()

print(r)