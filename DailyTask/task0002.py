# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月24日
将task0001中生成的激活码存储到mysql数据库当中
@author: mobydick46
'''
import mysql.connector
from time import sleep
 
#创建数据库库链接
conn=mysql.connector.connect(user="root",password="moonlight",database="pyTask", use_unicode=True)
#创建数据库操作游标
cur=conn.cursor()

drop_table="drop table if exists ActivateCode"
create_table='''
 create table If Not Exists ActivateCode(
     ID int auto_increment primary key,
     Code varchar(25) not null
 )
 '''

def insert_code(code):
    insert_data="insert into ActivateCode(Code) values ('%s')" % (code)
    cur.execute(insert_data)

def read_line(fp):
    '''
    按行读取激活码，去掉换行符
    '''
    with open(fp,'rb') as f:
        while True:
            line=f.readline().split('\n')[0]
            if line:
                yield line
            else:
                return

#创建激活码表
cur.execute(drop_table)
cur.execute(create_table)
#插入数据前先清空
cur.execute("delete from ActivateCode")
for line in read_line('code.txt'):
    for code in line.split(" "):
        if code:
            insert_code(code)

#左右操作必须提交事务之后才能生效
conn.commit()

#查询前五行记录
def select_lines(num):
    sql="select * from ActivateCode limit %d"%num
    cur.execute(sql)
    return cur.fetchall()

print select_lines(5)
cur.close()
print 'Done'

    

