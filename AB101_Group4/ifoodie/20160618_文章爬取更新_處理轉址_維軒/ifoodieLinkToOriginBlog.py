# coding=utf-8
# 使python可以讀取中文

import requests
from bs4 import BeautifulSoup as bs
import uniout


head = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

def ifoodieLinkToOriginBlog(urlIn):
   res=requests.get(urlIn,headers=head)
   res.encoding='utf-8'
   soup=bs(res.text,'lxml')
   linkList=soup.select('#restaurant_info a')
   return soup.findAll('a', href=True, target='_blank',rel='nofollow')[0].get('href')# 取得<a>並且屬性attr='1'
def main():
   url='https://ifoodie.tw/post/53bb4d2dc5904a000000001e'
   print ifoodieLinkToOriginBlog(url)
   


if __name__== "__main__":
    main()
    