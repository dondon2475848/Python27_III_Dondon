# coding=utf-8
# 使python可以讀取中文
### 印出字典的key與value########
def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key,'  :  ', value
########################    


import requests
from bs4 import  BeautifulSoup as bs
# import math
import re
#最後將travel List存到此字典
bigDic={}
# 放各個行程
travel=[]
# 裝各別形成的資料
dic={}


bid_detail = requests.get('http://vacation.eztravel.com.tw/pkgfrn/introduction/VDR0000001888/NGO04160602A')
soup2 = bs(bid_detail.text, "lxml")
row = soup2.select('div#pkgfrnVisitHistory')[0]
price = re.search('\d+', row.select('.price')[0].text)
plane= re.search('.{4}', row.select('div#flight-block1 span')[3].text)
# print row.select('div.pro-title.css-td h1')[0].text
# print price.group(0)
# print row.select('.tag')[0].text     
# print row.select('div#flight-block1 span')[2].text
# print plane.group(0)
# print row.select('div.day-box h4')[0].text      
# print row.select('div.day-box h4')[1].text
# print row.select('div.day-box h4')[2].text
# print row.select('div.day-box h4')[3].text
# print row.select('div.pro-id-right.css-td span')[0].text.strip() + ' ' +row.select('div.pro-id-right.css-td span')[1].text.strip()

dic['title']=row.select('div.pro-title.css-td h1')[0].text
dic['price']=price.group(0)
dic['city']=row.select('.tag')[0].text     
dic['time']=row.select('div#flight-block1 span')[2].text
dic['day1']=row.select('div.day-box h4')[0].text      
dic['day2']=row.select('div.day-box h4')[1].text 
dic['day3']=row.select('div.day-box h4')[2].text
dic['day4']=row.select('div.day-box h4')[3].text
dic['planeCom']=plane.group(0)
dic['pid1']=row.select('div.pro-id-right.css-td span')[0].text.strip() 
dic['pid2']=row.select('div.pro-id-right.css-td span')[1].text.strip()


PrintKeyValue(dic)
travel.append(dic)
bigDic['travel']=travel
print bigDic




