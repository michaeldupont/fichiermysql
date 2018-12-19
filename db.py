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
        line=f.readline()
        if not data:
            break
        words = line.split(";")
        print(words)
        db=_mysql.connect(host="localhost",user="chnordfr_mike", passwd="Ezwof01d!",db="chnordfr_python")
        db.query("""INSERT INTO `test`(`number`, `date1`, `date2`, `nom1`, `prenom`,
                 `L2`, `L3`, `L4`, `L5`, `CP`, `loc`) VALUES (NULL,'words[0]','words[1]','words[2]','words[3]',
                 'words[4]','words[5]','words[6]','words[7]','words[8]','words[9]','words[10],words[11]') """)
        r=db.store_result()
            print("ligne",r)

############ gestion de la base de données mysql : écriture du fichier en base



