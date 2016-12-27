#!/usr/bin/env python
# coding: utf-8
# moz_cookill.py  
# Destruction ciblée des cookies dans Firefox

import os,sys
import sqlite3 as sql
from socket import gethostname   

if sys.platform=='linux' or sys.platform=='linux2':
    path="~/.mozilla"
elif sys.platform=="darwin":
    path="~/Library"
else:
    print('%s not supported'%sys.platform)
    sys.exit(0)

for i,j,f in os.walk(os.path.expanduser(path)):
    if 'cookies.sqlite' in f:
        dat=os.path.join(i,'cookies.sqlite')

try:
    db=sql.connect(dat)
except:
    print("ERREUR : Firefox n'est peut-être pas installé sur %s ..."%gethostname())   
    sys.exit()
c=db.cursor()

while True:
    c.execute('SELECT baseDomain FROM moz_cookies;')
    aff=c.fetchall()

    ls=[]
    for i in aff:
        ls.append(str(i[0]))    # dom.com au lieu de (u'dom.com',)
    ls1=[]
    for i in ls:
        if i not in ls1:
            ls1.append(i)       # liste sans doublon
    for i in sorted(ls1):          
        print(i)                # affichage trié

    print('\nSortie si vide')
    cook=raw_input('Suppression des cookies du domaine : ')
    if cook=="":
        break
    req='DELETE FROM moz_cookies WHERE baseDomain LIKE '+'"%'+cook+'%"'+';'
    c.execute(req)
    db.commit()

print('Fin du programme')

# Écrit par cerulean  <ceruleanfirm@gmail.com>  0x71F86DC1B12845E9
# Nov. 2016
# Free For All

