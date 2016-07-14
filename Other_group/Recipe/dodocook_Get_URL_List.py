# coding=utf-8
# 使python可以讀取中文

###import
import requests
import os
from bs4 import  BeautifulSoup as bs
import json

### function(def) 宣告區######################################################################

### 創立資料夾的function########
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path
########################





###main
link_list=[]
for i in range(1,1904) :
    res=requests.get('http://www.dodocook.com/recipes/category/0/{0}/new'.format(i))
    # print res.text
    # print type(res.text)
    # type:unicode
    # <type 'unicode'>
    
    soup = bs(res.text, "lxml") 
    # print type(soup)
    #<class 'bs4.BeautifulSoup'>
    soup2 = soup.select('div.StBox')
    # print soup2
    # print type(soup2)
    #<type 'list'>
    # print soup2[0]
    # print type(soup2[0])
    #<class 'bs4.element.Tag'>

    for a in soup2[0].select('a.Cna'):
        #print 'http://www.dodocook.com/'+a['href'] 
        #a['href']  <type 'str'>
        link='http://www.dodocook.com/'+a['href'] 
        link_list.append(link)
    print len(link_list) 
mkdir('./data')
with open('./data/link_list.json' , 'w') as f:        
    json.dump(link_list, f)
    






