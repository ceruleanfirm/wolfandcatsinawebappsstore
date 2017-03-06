#!/usr/bin/env python
# find_db.py

import os, sqlite3
from sys import exit

path=raw_input('Path : ')
f_db=raw_input('Database file : ')

try:
    for rac,rep,fic in os.walk(os.path.expanduser(path)):
        if f_db in fic:
            dat=os.path.join(rac,f_db)
            print(dat)

    db=sqlite3.connect(dat)
    c=db.cursor()

    print('\nDATABASE : '+f_db.encode()) 
    c.execute('SELECT * FROM SQLite_MASTER;')
    while True:
        print
        for i in c.fetchall():
            print(i)
        tab=raw_input('\n\tTABLE NAME : ')
        if tab=="":
            break
        c.execute('SELECT * FROM '+tab)
        for i in c.fetchall():
            print(i)
            
    exit(0)   

except NameError:
    print('"%s" not found ...'%f_db)
    exit(1) 
