# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('./.userDB.sqlite3')
c = conn.cursor()
http= "%http%"

c.execute('create table users (username unique, password, registered_on)')
#c.execute('delete from uniquser')
#c.execute('select * from uniquser')
#c.execute('select * from uniquser where TEXT like "%s"' %http)
conn.commit()

"""e=0
for row in c:
   for i in row:
      print i
   e+=1
print e"""
