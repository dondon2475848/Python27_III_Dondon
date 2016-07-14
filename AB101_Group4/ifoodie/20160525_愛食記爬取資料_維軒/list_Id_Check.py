# -*- coding: utf-8 -*-
import json


# 讀檔：使用者清單，已預先抓好，約29萬筆
with open('./data/userlist.json','r') as f:
    userlist = json.load(f)
	
userList2=userlist['users']
# print len(userList2)
# print userList2.index('566b717f2756dd651db3c97a')
# print userList2[294691]