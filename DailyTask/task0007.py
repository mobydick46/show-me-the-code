# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月25日
统计代码中的实际代码、空行和注释
@author: mobydick46
'''

linenum=0
#统计代码行数
code_count=dict()
code_count["code"]=0
code_count["empty_line"]=0
code_count["text"]=0

def find_next(f,line):
    #简单化处理：
    #1.单行注释
    #2.多行注释
    global linenum
    if line.endswith(r"'''") and len(line)>3:
        return
    for line in f.xreadlines():
        line=line.strip()  #去除两边的空字符
        linenum+=1
        if line.startswith(r"'''"):
            return

with open('task0007.py','rb') as f:
    for line in f.xreadlines():
        line=line.strip()  #去除两边的空字符
        linenum+=1
        if line.startswith('#'):
            code_count["text"]+=1
        elif line.startswith(r"'''"):
            begin=linenum
            find_next(f,line)
            code_count["text"]+=(linenum-begin+1)
        elif len(line.strip())==0:
            code_count["empty_line"]+=1
        else:
            code_count["code"]+=1
print code_count