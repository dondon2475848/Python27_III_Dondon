# -*- coding: utf-8 -*-


import re
import requests
from bs4 import BeautifulSoup as bs

###去除標點符號及數字(僅保留中英文，含全型與半型)
def removePunctuation(source):
    xx = u'([^a-z^A-Z^ａ-ｚ^Ａ-Ｚ^\u4e00-\u9fff]+)'
    s = re.sub(xx,' ',source)
    return s.encode('utf8')
	
#.    任何字元,數字,符號,及空格
# \w    任何字元,數字
# \d    任何數字
# \s    任何空格
# +    1個或1個以上
# *    0個或0個以上

def  pixnetGetContent_A(urlIn):
	res = requests.get(urlIn)
	res.encoding = 'utf-8'
	soup = bs(res.text,'html.parser')
	#去除script標籤
	[x.extract() for x in soup.select('script')]
	#去除a標籤
	[x.extract() for x in soup.select('a')]
	art = soup.select('.article-content-inner')
	#將標籤內的文字加到list
	line = [a.text for a in art if a.text!=""]
	#去除空格以及垃圾(需建垃圾清單)
	st = "".join("".join(line).split()).replace(u'延伸閱讀','').replace('^','')
	st2='ＺＺＺ'+st
	print st.encode('utf8')
	#去除標點符號及數字 
	print removePunctuation(st)

	
pixnetGetContent_A('http://cosxsmallu.pixnet.net/blog/post/42778853')