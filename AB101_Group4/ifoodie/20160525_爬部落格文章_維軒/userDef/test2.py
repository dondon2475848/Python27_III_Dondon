# coding=utf-8
# 使python可以讀取中文
import re


def removePunctuation(source):
    xx = u'([^a-z^A-Z^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    # u4E00為中文的第一個字：一 u9FCC為中文的最後一個字：鿌
    # Unocode可以參考：
    # https://ja.wikipedia.org/wiki/Unicode%E4%B8%80%E8%A6%A7_4000-4FFF
    s = re.sub(xx,' ',source)
    return s
    
    
    

# print removePunctuation('1234AZaz  '+u'\uFF21\uFF3A\uFF41\uFF5A\u4E00\u9FCC')
# print '咚咚'