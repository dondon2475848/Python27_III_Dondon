# coding=utf-8
# 使python可以讀取中文


# In[11]:

import requests
from bs4 import  BeautifulSoup as bs
import math
import re


# In[4]:

rs = requests.session()
res = rs.get('http://vacation.eztravel.com.tw/pkgfrn/results/TPE/49?fullStatus=NONE')
soup = bs(res.text)


# In[8]:

count  = soup.select('.v-line')[0].text.split(' ')
print count[1]
page = int(math.ceil(float(count[1]) / 18))
print page


# In[7]:

urlFormat = 'http://vacation.eztravel.com.tw/pkgfrn/results/TPE/49/{}?&fullStatus=NONE'
with open('E:\\BigData\\Project\\Travel\\EZTravel_Link\\bid_list_for_EZtravel_in_Shikoku.txt','w') as f:
    for pageNum in range(1,page+1):
        url = urlFormat.format(pageNum)
        res2 = rs.get(url)
        soup1 = bs(res2.text)
        list_table = soup1.select('div#listTable')[0]
        for items in list_table.select('div.list-box.mainLinkBox'):
            f.write('http://vacation.eztravel.com.tw/pkgfrn/' + items.select('a')[0]['href'].split('/pkgfrn/')[1] + '\n')


# In[9]:

str = 'http://vacation.eztravel.com.tw/pkgfrn/introduction/FRN0000014050/20160524'
get = str.split('/')
print get


# In[10]:

dic = {} #宣告一個dic，稍後會將檔名(Key)跟網址(Value)一一放入
for bid_url in open('E:\\BigData\\Project\\Travel\\EZTravel_Link\\bid_list_for_EZtravel_in_Shikoku.txt','r'):
    splitStr = bid_url.split('/')
    dataName = splitStr[5].strip() + "_" + splitStr[6].strip()
    if dataName not in dic:
        dic[dataName] = bid_url
    else:
        print dataName,dic[dataName]
#     print dataName


# In[3]:

for bid_url in open('E:\\BigData\\Project\\Travel\\EZTravel_Link\\bid_list_for_EZtravel_in_Shikoku.txt','r'):
    bid_detail = requests.get(bid_url.strip())
    soup2 = bs(bid_detail.text)
    print soup2.select('div.row')[0]


# In[40]:

# with open('D:\\Big Data\\Project\\Travel\\EZtravel\\Link\\bid_list_for_EZtravel_in_Shikoku.txt','r'):
dic = {
    'Title':'', #單筆
    'Price':'', #單筆
    'Area':'', #單筆
    'Plane':'', #單筆
    'DepartureTime':'', #單筆
    'Hotel':'', #分多筆
    'Tourism':'', #分多筆
    'Item ID':'' #單筆
}
dicHot = {
    'Day1':'',
    'Day2':'',
    'Day3':'',
    'Day4':'',
#     'Day5':'',
#     'Day6':'',
#     'Day7':''
}
dicTour = {
    'Day1':'',
    'Day2':'',
    'Day3':'',
    'Day4':'',
#     'Day5':'',
#     'Day6':'',
#     'Day7':''
}
bid_detail = requests.get('http://vacation.eztravel.com.tw/pkgfrn/introduction/VDR0000001888/NGO04160602A')
soup2 = bs(bid_detail.text)
row = soup2.select('div#pkgfrnVisitHistory')[0]
price = re.search('\d+', row.select('.price')[0].text)
plane= re.search('.{4}', row.select('div#flight-block1 span')[3].text)
print row.select('div.pro-title.css-td h1')[0].text, price.group(0), row.select('.tag')[0].text,      row.select('div#flight-block1 span')[2].text, plane.group(0), row.select('div.day-box h4')[0].text,      row.select('div.day-box h4')[1].text, row.select('div.day-box h4')[2].text, row.select('div.day-box h4')[3].text
print row.select('div.pro-id-right.css-td span')[0].text.strip() + ' ' +row.select('div.pro-id-right.css-td span')[1].text.strip()



