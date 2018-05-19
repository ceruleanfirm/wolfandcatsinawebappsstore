#!/usr/bin/env python
# coding: utf-8
# chromdelhistcookill.py  # test

import os, sqlite3, sys
from tldextract import extract          ## comment if no tldextract
from socket import gethostname


def find_db(path,dbname):
    for rac,rep,fic in os.walk(os.path.expanduser(path)):
        if dbname in fic:
            dat=os.path.join(rac,dbname)
	return dat

def delhist():
    print('\n\n\t\tPHASE DE SUPRESSION DE L\'HISTORIQUE DE CHROME')
    print('\t\t\tChrome doit être fermé ...')
    k=raw_input('\nkill des processus chrome.\nContinuer (O/n) ? : ')
    if k.lower().startswith('n'):
	    print('Abandon ...')
	    exit()
    else:
        os.system('pkill chrom 2>/dev/null')
        os.system('killall chromium 2>/dev/null')

    print('\nRecherche de l\'historique de Chrome ...\n')
    try:
    	db2=sqlite3.connect(history)
    	c2=db2.cursor()
    except Exception as e:
    	print(e)
    	exit(2)
    print('\n\t1 - Supprimer tout l\'historique')
    print('\t2 - Suppression ciblée (domaine ou recherche)')
    print('\t3 - Quitter\n')
    chx=raw_input("Faites votre choix : ")
    if chx=='1':
    	ls=["urls","keyword_search_terms","segments"]
    	for i in ls:
    		c2.execute('DELETE FROM %s'%i)
    		db2.commit()
    	print('Historique supprimé.')
    elif chx=='2':
    	print
    	c2.execute('SELECT * FROM urls')
    	for i in c2.fetchall(): print(i[1])  
    	print('\n\t\tHistorique par domaines\n')
    	while True:
    		chaine=raw_input('\nSuppression de l\'historique contenant la chaine de caractères : ')
    		if not chaine :break
    		req='DELETE FROM urls WHERE url LIKE '+'"%'+chaine+'%"'
    		req3='DELETE FROM segments WHERE name LIKE '+'"%'+chaine+'%"'
    		try:
    			c2.execute(req)
    			c2.execute(req3)
    		except Exception as e:
    			print(e)
    			pass
    		finally:
    			db2.commit()
    		
    	print
    	c2.execute('SELECT * FROM keyword_search_terms')
    	for i in c2.fetchall(): print(i[2])  
    	print('\n\t\tHistorique des recherches\n')
    	while True:
    		chaine=raw_input('\nSuppression des recherches contenant la chaine de caractères : ')
    		if not chaine :break
    		req='DELETE FROM keyword_search_terms WHERE term LIKE '+'"%'+chaine+'%"'
    		try:
    			c2.execute(req)
    		except Exception as e:
    			print(e)
    			pass
    		finally:
    			db2.commit()
    else:
    	pass
    print('\nFin du programme.')
    exit()

if sys.platform.startswith("linux"):
    path=os.path.expanduser("~/.config/chromium/Default/")
elif sys.platform=="darwin":
    path="~/Library"
else:
    print('%s not supported'%sys.platform)
    sys.exit(0)

cookies=find_db(path,"Cookies")
history=find_db(path,"History")

try:
    db=sqlite3.connect(cookies)
except:
    print('Chrome n\'est peut-être pas installé sur %s ...'%gethostname())
    sys.exit(0)
c=db.cursor()

print('\n\n\t\tPHASE DE SUPRESSION DES COOKIES DANS CHROME\n')
print('\nTuez-les tous ? (Entrez "KILLEMALL")')
print('ATTENTION, cette action détruira TOUS les cookies enregistrés dans chrome.')
print('\nDestruction par domaine ? (Entrez "D")')
rep=raw_input('  >>  ')
if rep.startswith('KILLEM'):
    c.execute('DELETE FROM cookies;')
    db.commit()
    print('\nCookies effacés.')
    delhist()

while True:
    c.execute('SELECT host_key FROM cookies;')
    tab=c.fetchall()

    ls0=[]
    for i in tab:
        ls0.append(str(i[0]))
    ls1=[]                          ## comment if no tldextract
    for i in ls0:                   ## ...
        j=extract(i)                ## ...
        ls1.append('.'.join(j[1:])) ## ...
    ls2=[]
    for i in sorted(ls1):           ## ls0 if no tldextract ...
        if i not in ls2:
            ls2.append(i)
    for i in ls2:
        print(i)

    print('\nSortie si vide')
    cook=raw_input('Suppression des cookies du domaine : ')
    if cook=="":
        break
    req='DELETE FROM cookies WHERE host_key LIKE '+'"%'+cook+'%"'+';'
    c.execute(req)
    db.commit()

delhist()

# Écrit par cerulean  <ceruleanfirm@gmail.com>  0x71F86DC1B12845E9
# Free For All

