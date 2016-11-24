#!/usr/bin/env python
# coding: utf-8
# cookillemoz.py  
# Permet de voir des trucs effrayants, et de pouvoir les éliminer !

import os,sys
import sqlite3 as sql
from socket import gethostname

#dat=os.path.expanduser('~/tmp/cookies.sqlite')

for rac,reps,fics in os.walk(os.path.expanduser("~/.mozilla")): # test sur fichier temp ...
    if 'cookies.sqlite' in fics:
        dat=os.path.join(rac,'cookies.sqlite')

try:        
    db=sql.connect(dat)
except:
    print('Firefox semble ne pas être installé sur %s ...'%gethostname())
    sys.exit()
c=db.cursor()

print('\nTuez-les tous ? (Entrez "KILL")')
print('ATTENTION, cette action détruira TOUS les cookies enregistrés dans Firefox.')
print('\nDestruction par domaine ? (Entrez "D")')
rep=raw_input(" >> ")

if rep.lower().startswith('kill'):
    c.execute('DELETE FROM moz_cookies;')
    db.commit()
    print("Programme Terminé.")
    sys.exit(0)

while True:
    c.execute('SELECT baseDomain FROM moz_cookies;')
    aff=c.fetchall()

    ls=[]
    for i in aff:
        ls.append(str(i[0]))    # dom.com au lieu de (u'dom.com',)
    ls1=[]
    for i in sorted(ls):
        if i not in ls1:
            ls1.append(i)       # liste sans doublon
    for i in ls1:          
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

