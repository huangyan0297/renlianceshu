# -*- coding:utf-8 -*-

import MySQLdb

id=int(input("请输入班级ID"))
from c1 import fc1
a=fc1()

from c2 import fc2
b=fc2()

from c3 import fc3
c=fc3()



cxn = MySQLdb.Connect(host = '192.168.1.109', user = 'root', passwd = 'test')
cur = cxn.cursor()
cur.execute("USE zldb")

# SQL 查询语句
sql = "SELECT * FROM kc \
       WHERE id  = '%d'" % (id)
cur.execute(sql)
results = cur.fetchall()
for row in results:
	t = row[1]

#a1=t-a
#a2=(t-a)/t
#b1=b-a
#b2=(b-a)/t
#c1=b-c
#c2=(b-c)/t

cur.execute("INSERT INTO count VALUES(%d,%d,%d,%f,%d,%d,%f,%d,%d,%f)"%(id,a,t-a,(t-a)*100/t,b,b-a,(b-a)*100/t,c,b-c,(b-c)*100/t))

cur.close()
cxn.commit()
cur.close()

