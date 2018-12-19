# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:35:46 2018

@author: fmdu
"""

import os
import mysql.connector as mariadb


def inputdb(line):
    words = line.split(";")
    mariadb_connection = mariadb.connect(user='chnordfr_mike', password='Ezwof01d!', database='chnordfr_python')
    cursor = mariadb_connection.cursor()
    cursor.execute("INSERT INTO `test`(`number`, \
        `date1`, `date2`, `civ`, `nom1`, `prenom`, `L2`, `L3`, `L4`, `L5`, `CP`, `loc`) \
        VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (words[0], words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10]))
    mariadb_connection.commit()
    mariadb_connection.close()

############ ouverture de fichier et lecture

with open('data_test.txt', 'r') as mon_fichier:
    print("nom du fichier", mon_fichier.name)
    while 1:
        ligne=mon_fichier.readline()
        if ligne =="":
            break
        inputdb(ligne)


