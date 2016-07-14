# -*- coding: utf-8 -*-
import json
import os
from userDef.pixnet import pixnetA
from userDef.reUser import retainEnglishChinese



### Def 宣告
# 創立資料夾(會檢查資料夾是否存在)
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path
# 印出字典的key與value
def printKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key,'  :  ', value




# 讀檔：使用者清單，已預先抓好，約29萬筆使用者的部落格文章資料
with open('./data/ifoodBlog_270000_270999.json','r') as f:
    blogList = json.load(f)
    list2=blogList['blog']
    
print list2
# print list[0]['blog_type']
url = list2[0]['url']
url2 = list2[1]['url']
print url
print retainEnglishChinese(pixnetA(url))
print url2
print retainEnglishChinese(pixnetA(url2))
