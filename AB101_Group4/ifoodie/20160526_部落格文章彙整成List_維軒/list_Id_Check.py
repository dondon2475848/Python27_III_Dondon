# -*- coding: utf-8 -*-
import json


# 讀檔：使用者清單，已預先抓好，約29萬筆
with open('./data/blog/article/listAllArticle.json','r') as f:
    listAllArticle = json.load(f)
	
# 20160524抓的資料有72838篇文章
print len(listAllArticle)
# print userList2.index('566b717f2756dd651db3c97a')
# print userList2[294691]