#!/usr/bin/env python
# coding: utf-8
# cookillemoz.py

import os,sys
import sqlite3 as sql
from socket import gethostname

if sys.platform.startswith("linux"):
    path='~/.mozilla'
elif sys.platform=="darwin":
    path="~/Library"
else:
    print('%s not supported'%sys.platform)
    exit(1)

def find_db(path,dbname):
	for i,j,k in os.walk(os.path.expanduser(path)):
		if dbname in k:
			dat=os.path.join(i,dbname)
	return dat

cookies=find_db(path,'cookies.sqlite')

try:        
    db=sql.connect(cookies)
except:
    print("ERREUR : Firefox n'est peut-être pas installé sur %s ..."%gethostname())
    exit(2)
c=db.cursor()
print('\n\n\t\tPROGRAMME DE SUPPRESSION DES COOKIES DANS FIREFOX\n')
print('\nTuez-les tous ? (Entrez "KILLEMALL")')
print('ATTENTION, cette action détruira TOUS les cookies enregistrés dans Firefox.')
print('\nDestruction par domaine ? (Entrez "D")')
rep=raw_input(" >> ")

if rep.startswith('KILLEM'):
	c.execute('DELETE FROM moz_cookies;')
	print('cookies effacés.')
	db.commit()
	hist=raw_input('Effacer tout l\'historique (N/o) : ')
	if hist.lower().startswith('o'):
		history=find_db(path,'places.sqlite')
		db2=sql.connect(history)
		c2=db2.cursor()
		ls=["moz_places","moz_hosts","moz_historyvisits","moz_inputhistory","moz_favicons"]
		for i in ls:
			c2=db2.cursor()
			c2.execute('delete from %s'%i)
			db2.commit()
		print('Historique effacé.')
	print("Programme Terminé.")
	sys.exit(0)

while True:
    c.execute('SELECT baseDomain FROM moz_cookies;')
    aff=c.fetchall()

    ls=[]
    for i in aff:
        ls.append(str(i[0])) 
    ls1=[]
    for i in sorted(ls):
        if i not in ls1:
            ls1.append(i)     
    for i in ls1:          
        print(i)               

    print('\nSortie si vide')
    cook=raw_input('Suppression des cookies du domaine : ')
    if cook=="":
        break
    req='DELETE FROM moz_cookies WHERE baseDomain LIKE '+'"%'+cook+'%"'+';'
    c.execute(req)
    db.commit()

print('Fin du programme')

# Écrit par cerulean  <ceruleanfirm@gmail.com>  0x71F86DC1B12845E9
# Free For All

