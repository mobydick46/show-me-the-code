# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月23日
生成应用的激活码
@author: mobydick46
'''
import string
import random
from __builtin__ import int


def baseDic():
    '''
    返回激活码生成的空间域：字母+数字
    '''
    return string.letters+string.digits

def genActivateCode(len):
    '''
    根据给定的长度len生成一个激活码
    '''
    baseStr=baseDic()
    key=[random.choice(baseStr) for i in range(len)]
    return "".join(key)

num=raw_input("Please input the number of your activate codes:")
len=raw_input("Please input the length of your activate codes:")

#最终结果保存在文件当中
codeFile=open("code.txt",'w')
try:
    for i in range(1,int(num)+1):
        codeFile.write(genActivateCode(int(len))+" ")
        if i%10==0:
            codeFile.write("\n")
    codeFile.close()
except:
    print "Illegal input"
    
print "Done"



    