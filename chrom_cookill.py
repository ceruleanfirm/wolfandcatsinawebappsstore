#!/usr/bin/env python
# coding: utf-8
# chrom_cookill.py

import os, sqlite3, sys
from tldextract import extract          ## comment if no tldextract
from socket import gethostname


if sys.platform.startswith("linux"):
    dat=os.path.expanduser("~/.config/chromium/Default/Cookies")
elif sys.platform=="darwin":
    path="~/Library"
    for rac,rep,fic in os.walk(os.path.expanduser(path)):
        if "Cookies" in fic:
            dat=os.path.join(rac,"Cookies")
else:
    print('%s not supported'%sys.platform)
    sys.exit(0)

try:
    db=sqlite3.connect(dat)
except:
    print('Chrome n\'est peut-être pas installé sur %s ...'%gethostname())
    sys.exit(0)
c=db.cursor()

print('\n\n\t\tPROGRAMME DE SUPRESSION DES COOKIES DANS CHROME\n')
print('\nTuez-les tous ? (Entrez "KILLEMALL")')
print('ATTENTION, cette action détruira TOUS les cookies enregistrés dans chrome.')
print('\nDestruction par domaine ? (Entrez "D")')
rep=raw_input('  >>  ')
if rep.startswith('KILLEM'):
    c.execute('DELETE FROM cookies;')
    db.commit()
    print('Programme Terminé')
    sys.exit(0)

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
        print('Fin du Programme')
        break
    req='DELETE FROM cookies WHERE host_key LIKE '+'"%'+cook+'%"'+';'
    c.execute(req)
    db.commit()

# Écrit par cerulean  <ceruleanfirm@gmail.com>  0x71F86DC1B12845E9
# Nov. 2016
# Free For All

