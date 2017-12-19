#!/usr/bin/python
# coding: utf-8
import MySQLdb

a=8
b=5
#连接
cxn = MySQLdb.Connect(host = '172.20.10.12', user = 'root', passwd = 'test')
#游标
cur = cxn.cursor()


#创建数据库
cur.execute("USE PyTest")

#创建表
#插入
cur.execute("INSERT INTO users VALUES(%d,%d)"%(a,1))
#查询
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print('%s\t%s' %row)

#关闭
cur.close()
cxn.commit()
cxn.close()

