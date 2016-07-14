# coding=utf-8
import re

def retainEnglishChinese(dataIn):
    xx = u'([^a-z^A-Z^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    #u4E00為中文的第一個字：一 u9FCC為中文的最後一個字：鿌
    s = re.sub(xx,' ',dataIn)
    return s
    
    
def retainEnglishChinese2(dataIn):
    xx = '([^a-z^A-Z^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    #u4E00為中文的第一個字：一 u9FCC為中文的最後一個字：鿌
    s = re.sub(xx,' ',dataIn)
    return s
    
text=('1234AZaz  '+u'\uFF21\uFF3A\uFF41\uFF5A\u4E00'+u'咚咚')
print  retainEnglishChinese(text)
print  retainEnglishChinese2(text)

