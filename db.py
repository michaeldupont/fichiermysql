# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:34:09 2018

@author: fmdu
"""

import os
import _mysql


############ ouverture de fichier et lecture

with open('data_test.txt', 'r') as mon_fichier:
    print("nom du fichier", mon_fichier.name)
    while 1:
        line=mon_fichier.readline()
        if line =="":
            break
        words = line.split(";")
        for i in range(0,len(words)-1):
            print(words)
            print(words[i])
        db=_mysql.connect(host="localhost",user="chnordfr_mike", passwd="Ezwof01d!",db="chnordfr_python")
        
        requete = 
        data = 
        
        db.query("""INSERT INTO `test`(`number`, \
        `date1`, `date2`, `civ`, `nom1`, `prenom`, `L2`, `L3`, `L4`, `L5`, `CP`, `loc`) \
        VALUES (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (words[0], \
        words[1],words[2],words[3], words[4],words[5],words[6],words[7],words[8],words[9],words[10]))
        
        r=db.store_result()
        print("ligne",r)

############ gestion de la base de données mysql : écriture du fichier en base



