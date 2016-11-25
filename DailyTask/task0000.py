# -*- coding: UTF-8 -*-   
'''
Created on 2016年11月22日
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
@author: mobydick46
'''
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from __builtin__ import raw_input
from pango import Font

def drawNumber(fp,num):
    try:
        img=Image.open(fp)
        img_width=img.size[0]
        img_height=img.size[1]
        
        #单个字的大小、宽度
        font_size=img_height/8
        font_width=img_width/8
        
        font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf",font_size)
        
        #文本区域的坐标
        text_x=(img_width-font_width*len(str(num)))*0.9
        text_y=img_height*0.1
        draw=ImageDraw.Draw(img)
        draw.text((text_x,text_y),str(num),(255,0,0),font)
    
        img.show()
        
        #默认保存回源文件夹
        strs=fp.split("/")
        newfp=fp.replace(strs[-1],"newtask0000.jpg",1)
        img.save(newfp)
        img.close()
        print 'Done'
    except:
        print "file not found"
        
fp=raw_input("Please input the file name,including the complete path：")
try:
    s=raw_input("Please input the number：")
    num=int(s)
    drawNumber(fp, num)
except:
    print "Wrong number"

