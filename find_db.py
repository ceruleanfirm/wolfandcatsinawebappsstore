#!/usr/bin/env python
# coding: utf-8
# find_db.py
# Exploration des db sqlite

import os, sqlite3
from sys import exit

path=raw_input('Path : ')
f_db=raw_input('Database file : ')
try:
    for rac,rep,fic in os.walk(os.path.expanduser(path)):
        if f_db in fic:
            dat=os.path.join(rac,f_db)
except:
    print('%s not found ...'%f_db)
    exit(1) 
print dat

db=sqlite3.connect(dat)
c=db.cursor()

while True:
    print
    print('Database : '+f_db.encode()) 
    print
    c.execute('SELECT * FROM SQLite_MASTER;')
    for i in c.fetchall():
        print(i)
    tab=raw_input('\n\tTable name : ')
    if tab=="":
        break
    c.execute('SELECT * FROM '+tab)
    for i in c.fetchall():
        print(i)
        
exit(0)   
