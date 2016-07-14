# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
		
def  pixnetA(urlIn):
	res = requests.get(urlIn)
	res.encoding = 'utf-8'
	soup = bs(res.text,'html.parser')
	#去除script標籤
	[x.extract() for x in soup.select('script')]
	#去除a標籤
	[x.extract() for x in soup.select('a')]
	art = soup.select('.article-content-inner')
	#去除沒有內文的標籤，並將有內文的標籤去除，一筆筆加入
	line = [a.text for a in art if a.text!=""]
	#去除空格以及垃圾(需建垃圾清單)
	st = "".join("".join(line).split()).replace(u'延伸閱讀','').replace('^','')
	return st

	
