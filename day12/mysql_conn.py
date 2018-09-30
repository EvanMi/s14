# -*- coding:utf-8 -*-
# Author: Evan Mi
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='day12')
cursor = conn.cursor()
effect_row = cursor.executemany('insert into student(name,sex,register_date) values(%s,%s,%s)',
                                [('li1', 'F', '2018-03-22'), ('li2', 'F', '2018-03-22'), ('li3', 'F', '2018-03-22')])

effect_row = cursor.execute("select * from student")

print(cursor.fetchone())
print(cursor.fetchmany(2))
print(cursor.fetchall())

conn.commit()
conn.close()
