# -*- coding: utf-8 -*-
import json
# 印出字典的key與value
def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key.encode('utf8') ,'  :  ', value.encode('utf8')  



# 讀檔：使用者清單，已預先抓好，約29萬筆
with open('./data/listAllArticle_New_0_72838_v1.json','r') as f:
    listMerge_72838 = json.load(f)
	
# 20160524抓的資料有72838篇文章
print len(listMerge_72838)
dic=listMerge_72838[43719]
# PrintKeyValue(dic)

# print simplejson.dumps(dic, encoding="UTF-8", ensure_ascii=False)
# print json.dumps(dic, encoding="UTF-8", ensure_ascii=False)
print json.dumps(dic, encoding='UTF-8', ensure_ascii=False)

# print len(listMerge_72838[13902]['article'])
# print listAllArticle.index('566b717f2756dd651db3c97a')
# print userList2[294691]