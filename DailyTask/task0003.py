# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月25日
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
@author: mobydick46
'''
import redis

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

#获取redis数据库连接，线程安全
r=redis.Redis(host="localhost",port=6379,db=0)
#pipline 操作
p=r.pipeline()
#将激活码保存到集合当中
for line in read_line("code.txt"):
    for code in line.split(" "):
        if code:
            p.sadd("ActivateCode",code)
p.execute()
#保存到磁盘上
r.save()
print r.smembers("ActivateCode")