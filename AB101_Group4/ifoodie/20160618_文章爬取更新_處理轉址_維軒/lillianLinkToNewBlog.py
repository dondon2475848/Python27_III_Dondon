# coding=utf-8
# 使python可以讀取中文

import requests
from bs4 import BeautifulSoup as bs



head = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

def lillianLinkToNewBlog(urlIn):
   res=requests.get(urlIn,headers=head)
   res.encoding='utf-8'
   soup=bs(res.text,'lxml')
   #print res.text
   return soup.select('.pili a')[1].get('href')
def main():
   url='http://lillian1101.pixnet.net/blog/post/203524858-%e4%b8%ad%e5%b1%b1%e7%be%8e%e9%a3%9f%7c%e5%b9%b3%e5%83%b9%e8%b1%ac%e6%8e%92%e6%97%a5%e5%bc%8f%e9%a4%90%e5%bb%b3-%e6%99%82%e6%82%85%e6%a8%82-%e4%b8%8a%e7%8f%ad%e6%97%8f%e5%8d%88'

   print lillianLinkToNewBlog(url)
   


if __name__== "__main__":
    main()
    