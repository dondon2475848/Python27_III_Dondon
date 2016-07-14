# coding=utf-8
# 使python可以讀取中文
import os
import json
import re
import requests
from bs4 import BeautifulSoup as bs


# 創資料夾
def mkdir(path):
    if os.path.exist(path)==False:
        os.makesdirs(path)
        print '建立資料夾',path
# 印出字典的key與value
def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key,'  :  ', value        
# 輸出錯誤訊息 
def createLog(log, type1):
    date = time.strftime('%Y%m%d')
    with open('./data/log/%s_%s.txt' % (type1, date), 'a') as f:
        f.write(log+'\n')
    exceptCount+=1
# 取出英文、中文
def retain_English_Chinese(StrIn):
    Str_English_Chinese = u'([^a-z^A-Z^^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    #u4E00為中文的第一個字：一 u9FCC為中文的最後一個字
    strClean = re.sub(Str_English_Chinese,' ',StrIn)
    return strClean
# 刪除不需要的詞彙
def deleteBadWords(StrIn):
    Str_BadWords = u'(延伸閱讀|連絡方式|電話預約|電話|營業時間|週一|週二|週三|週四|週五|週六|週日|周一|周二|周三|周四|周五|周六|\
                                                        周日|假日|公休|平日|地址|粉絲團|星期|禮拜|時間限制)'
    strClean = re.sub(Str_BadWords,' ',StrIn)
    return strClean
# 移除指定tag
def removeTag(soup,tag):
    [x.extract() for x in soup.select(tag)]
# 取得文章內文
def  GetArticle(urlIn):
    res = requests.get(urlIn)
    res.encoding = 'utf-8'
    soup = bs(res.text,'html.parser')
    removeTag(soup,'script')
    removeTag(soup,'a')
    removeTag(soup,'.rank')
    removeTag(soup,'iframe')
    xuite = soup.select('.blogbody')
    pixnet = soup.select('.article-content-inner')
    ifoodie = soup.select('#blog_content')
    miha = soup.select('#content article p')
    banbi = soup.select('article')
    art = xuite+pixnet+ifoodie+miha+banbi
    #去除沒有內文的標籤，並將有內文的標籤去除，一筆筆加入
    line = [a.text for a in art if a.text!=""]
    st1 = "".join("".join(line).split())
    st2=deleteBadWords(st1)
    return retain_English_Chinese(st2)        


def main():
    with open('./data/blog/article/listAllArticle.json','r') as f:
        listAllArticle = json.load(f)
#     print len(listAllArticle)
#     print listAllArticle[0:10]
    for blog in listAllArticle[0:3]:
        blog['article'] = GetArticle(blog['url'])
        print blog['article']
        print type(blog['article'])






if __name__== "__main__":
    main()
    