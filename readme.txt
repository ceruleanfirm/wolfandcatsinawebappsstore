

About find_db.py 

Usage example :

who@what:~/PYTHON/utils-$ find ~/ -name "*.sql*"

/home/who/.config/filezilla/queue.sqlite3
/home/who/.mozilla/firefox/4exdp5gx.default/formhistory.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/cookies.sqlite?
/home/who/.mozilla/firefox/4exdp5gx.default/webappsstore.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/content-prefs.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/places.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/kinto.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/permissions.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/storage/permanent/indexeddb+++fx-devtools/idb/478967115deegvatroootlss--cans.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/storage/permanent/chrome/idb/2918063365piupsah.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/storage/default/https+++bitcoinmagazine.com/idb/993782502OBNDE__KSDISG_NLA.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/cookies.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/storage.sqlite
/home/who/.thunderbird/z63ixfwu.default/blist.sqlite
/home/who/.thunderbird/z63ixfwu.default/formhistory.sqlite
/home/who/.thunderbird/z63ixfwu.default/webappsstore.sqlite
/home/who/.thunderbird/z63ixfwu.default/calendar-data/local.sqlite
/home/who/.thunderbird/z63ixfwu.default/content-prefs.sqlite
/home/who/.thunderbird/z63ixfwu.default/places.sqlite
/home/who/.thunderbird/z63ixfwu.default/global-messages-db.sqlite
/home/who/.thunderbird/z63ixfwu.default/permissions.sqlite
/home/who/.thunderbird/z63ixfwu.default/cookies.sqlite
/home/who/.ipython/profile_default/history.sqlite
/home/who/.cache/gnome-documents/cookies.sqlite
/home/who/.cache/mozilla/firefox/4exdp5gx.default/OfflineCache/index.sqlite
who@what:~/PYTHON/utils-$ 


who@what:~/PYTHON/utils-$ ./find_db.py 
Path : /home/who/.mozilla
Database file : webappsstore.sqlite
/home/who/.mozilla/firefox/4exdp5gx.default/webappsstore.sqlite

DATABASE : webappsstore.sqlite

(u'table', u'webappsstore2', u'webappsstore2', 2, u'CREATE TABLE webappsstore2 (originAttributes TEXT, originKey TEXT, scope TEXT, key TEXT, value TEXT)')
(u'index', u'origin_key_index', u'webappsstore2', 3, u'CREATE UNIQUE INDEX origin_key_index ON webappsstore2(originAttributes, originKey, key)')

	TABLE NAME : webappsstore2

(u'', u'moc.wolfrevokcats.:http:80', u'moc.wolfrevokcats.:http:80', u'se:fkey', u'dda09101450552a7d5ebc2d49d49a334,1487674383')
(u'', u'moc.tluafrevres.:http:80', u'moc.tluafrevres.:http:80', u'se:fkey', u'dda09101450552a7d5ebc2d49d49a334,1488213193')
(u'', u'moc.buhtig.:https:443', u'moc.buhtig.:https:443', u'bundle-urls', u'{"frameworks.js":"https://assets-cdn.github.com/assets/frameworks-506169cb2fe76254b921e8c944dd406e5cab2d719e657eace8ada98486231472.js","github.js":"https://assets-cdn.github.com/assets/github-c306b0369be2b8830b868e2cb2c4e0761077c41d878087c96bd7d.js","frameworks.css":"https://assets-cdn.github.com/assets/frameworks-cbc96727d20305fd11971974f0ce00af316f709ce2ac8e1be409a.css","github.css":"https://assets-cdn.github.com/assets/github-68582bcd5cb4de0d904ab472e81b8d26c2b748dff46d7def7ce0e.css","site.css":"https://assets-cdn.github.com/assets/site-b0f9837b69e1e9cde3df40f961a6b04698f95f1aba729.css"}')
(u'', u'gro.aidepikiw.rf.:https:443', u'gro.aidepikiw.rf.:https:443', u'CentralNoticeKV|global|buckets', u'{"expiry":1493634523,"val":"2017 Steward Elections!86562400!4340!0*WikiMOOC_France_2017_2!86252800!4660!1*WikiFranca_MC17!88067140!5520!0"}')
(u'', u'gro.aidepikiw.rf.:https:443', u'gro.aidepikiw.rf.:https:443', u'CentralAuthAnon', u'1488710275296')
(u'', u'gro.aidepikiw.rf.:https:443', u'gro.aidepikiw.rf.:https:443', u'CentralNoticeKV|category|WikiFranca_MC17|impression_diet', u'{"expiry":1520159875,"val":{"seenCount":2,"waitCount":0,"waitUntil":1489023875130,"waitSeenCount":2}}')
(u'', u'gro.trecac.www.:http:80', u'gro.trecac.www.:http:80', u'google_experiment_mod', u'280')
(u'', u'gro.trecac.ikiw.:http:80', u'gro.trecac.ikiw.:http:80', u'google_experiment_mod', u'440')


