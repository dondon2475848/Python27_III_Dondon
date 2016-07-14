# coding=utf-8
# 收集美食類別的資料
# http://www.ipeen.com.tw/taiwan/channel/F
import requests

url='http://www.ipeen.com.tw/taiwan/channel/F'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
} 
res = requests.get(url, headers=headers)

# print res
# print res.text
if res.status_code==200:
    print "200 OK,請求已成功"

from bs4 import BeautifulSoup 
soup = BeautifulSoup(res.text, "lxml") 
table = soup.select('table.allCate')[0]
# print table

dic={}
for tr in table.select('tr'):
    key=[]
    class_name = tr.select('td.head a')[0].text
    #print tr.select('td.head a')[0].text
    for td2 in table.select('td.detail li'):
        #print td2.select('a')[0].text
        sub_class_name = td2.select('a')[0].text
        key.append(sub_class_name)
    dic.update({class_name:key})

# for key, value in dic.iteritems() :
#     print key, value

# 檢查資料預計存取的資料夾，如不存在，創立
import os
document = 'D://Dropbox/Big_data_develop_class/ETL/Workspace2/Python2.7_Project/ipeen/data/'
if  os.path.exists(document)==False:
    os.makedirs(document) 

# json資料寫入    
import json
dataname = 'class_and_subClass_Name'
with open(document+'/'+dataname+'.json', 'w') as f:
    json.dump(dic, f, encoding='utf-8' )
    print "資料",dataname,"已儲存於資料夾",document  




