# -*- coding: utf-8 -*-
import json
import os
import re
import requests
from bs4 import BeautifulSoup as bs


### Def 宣告
# 創立資料夾(會檢查資料夾是否存在)
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path
# 印出字典的key與value
def printKeyValue(dicIn):
    for key, value in dicIn.iteritems() :
        print key,'  :  ', value
def retain_English_Chinese(StrIn):
    Str_English_Chinese = u'([^a-z^A-Z^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    #u4E00為中文的第一個字：一 u9FCC為中文的最後一個字：鿌
    strClean = re.sub(Str_English_Chinese,' ',StrIn)
    return strClean
def removeTag(soup,tag):
    [x.extract() for x in soup.select(tag)]
def  GetArticle(urlIn):
    res = requests.get(urlIn)
    res.encoding = 'utf-8'
    soup = bs(res.text,'html.parser')
    removeTag(soup,'script')
    removeTag(soup,'a')
    removeTag(soup,'.rank')
    removeTag(soup,'iframe')
    xuite = soup.select('.blogbody')
    pixnet = soup.select('.article-content-inner')
    ifoodie = soup.select('#blog_content')
    miha = soup.select('#content article p')
    banbi = soup.select('article')
    art = xuite+pixnet+ifoodie+miha+banbi
    #去除沒有內文的標籤，並將有內文的標籤去除，一筆筆加入
    line = [a.text for a in art if a.text!=""]
    st = "".join("".join(line).split()).replace(u'延伸閱讀','').replace('^','')
    print 'Url: '+urlIn
    print retain_English_Chinese(st)
 

#############################
############萬用版############
#############################
# http://blog.xuite.net/ca062/blog/413854020
# http://yao55.pixnet.net/blog/post/31422842
# https://ifoodie.tw/post/573c6fa92756dd04749b8ab2
# https://miha.tw/tp-vegetejiya/
# https://banbi.tw/weichi-sweets/

GetArticle('http://blog.xuite.net/ca062/blog/413854020')
