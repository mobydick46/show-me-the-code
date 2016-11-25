# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月25日
任一个英文的纯文本文件，统计其中的单词出现的个数
@author: mobydick46
'''
import string
from _weakref import getweakrefcount

basestr=string.letters+string.digits
word_count=dict()

def read_line(fp):
    '''
    按行读取激活码，去掉换行符
    '''
    with open(fp,'rb') as f:
        while True:
            line=f.readline()
            if line:
                if line.split('\n')[0]:
                    yield line.split('\n')[0]
            else:
                return
        
def getWord(fp):
    #从一行字符串中解析不同的单词
    word=""
    for line in read_line(fp):
        for each in line:
            if each in basestr:
                word+=each
            else:
                if word:
                    yield word
                word=""

for word in getWord("eng.txt"):
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

with open("word_count.txt",'wb') as rf:
    for tup in sorted(word_count.items(), lambda x, y: cmp(x[1], y[1]),reverse=True):
        rf.write(tup[0]+":"+str(tup[1])+"\n")

print 'Done'
    
            