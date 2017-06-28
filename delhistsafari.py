#!/usr/bin/env python
# coding: utf-8
# delhistsafari.py

import sqlite3, sys, os
from time import sleep

os.system('clear')
print('')
if sys.platform=="darwin":
	path="~/Library/Safari"
else:
    print('%s not supported.'%sys.platform)
    sys.exit()

for r,d,f in os.walk(os.path.expanduser(path)):
    if "History.db" in f:
        dat=os.path.join(r,"History.db")

try:
    db=sqlite3.connect(dat)
    c=db.cursor()
    c.execute('SELECT * FROM history_items;')
    for i in c.fetchall():
    	print(i[1])
    print('\n\n\tHISTORIQUE DES RECHERCHES ...\n')
    sleep(2)	
    ls=[]
    ls2=[]
    c.execute('SELECT * FROM history_visits;')
    for i in c.fetchall():
        ls.append(i[3])
    for i in ls:
        if i not in ls2:
    	    ls2.append(i)
    for i in ls2:		# liste sans doublon
        print(i)

except sqlite3.Error, e:
    #print('%s not found ...'%dat)
    print(e)
    sys.exit(2)

print('\n\t1. Suppression de tout l\'historique de Safari')
print('\t2. Suppression ciblée (domaine ou recherche)')
print('\t3. Quitter\n')
chx=raw_input('Faites votre choix : ')
if chx=="1":
    rep=raw_input("\n\nSouhaitez-vous supprimer tout l\'historique de navigation ? (N/o) : ")
    if rep=="o" or rep=="O":
        print('Entrez "OUI" ou "YES"')
        rep=raw_input(' >> ')
    if rep=="OUI" or rep=="YES":
        c.execute('DELETE FROM history_items;')
        db.commit()
        c.execute('DELETE FROM history_visits;')
        db.commit()
        print('\nLa suppression sera effective au prochain lancement de Safari ...')
	os.system('pkill Safari')
        print('\nProgramme terminé\n')
        sys.exit()
    #elif rep=="" or rep.lower().startswith('n'):
    else:
	print('Abandon')
        sys.exit()
elif chx=="2":
    print('')
    while True:
        chaine=raw_input('Suppression de l\'historique contenant la chaine de caractères (domaine ou mot-clé) : ')
        if not chaine:
	    break
        req='DELETE FROM history_visits WHERE title LIKE '+'"%'+chaine+'%"'
        c.execute(req)
        req2='DELETE FROM history_items WHERE url LIKE '+'"%'+chaine+'%"'
	c.execute(req2)
        db.commit()
    print('\nLa suppression sera effective au prochain lancement de Safari ...')
    os.system('pkill Safari')
    print('\nProgramme terminé\n')
else:
    print('\nFin du programme\n')
    sys.exit()


