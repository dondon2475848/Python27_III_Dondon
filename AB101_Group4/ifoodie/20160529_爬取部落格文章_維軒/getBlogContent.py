# coding=utf-8
# 使python可以讀取中文
import os
import json
import re
import requests
from bs4 import BeautifulSoup as bs
import random


# Variable
head = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

brand=['HTC','Sony','Asus','Acer','Samsung','LG','Motorola','InFocus','GSmart','OPPO','TWM','OKWAP','HUAWEI']
model=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

headRandom = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.{0}.{1};{2} {3}{4}-{5}{6}) \
AppleWebKit/537.36 (KHTML, like Gecko) Version/{7}.0 Chrome/30.0.0.0 Mobile Safari/537.36"\
.format(random.randint(0,9),random.randint(0,9),brand[random.randint(0,len(brand)-1)],\
model[random.randint(0,len(model)-1)],random.randint(1,99),model[random.randint(0,len(model)-1)],\
random.randint(799,1599),random.randint(250,9999))
}
# 取出英文、中文
def retain_English_Chinese_Arabic_numerals(StrIn):
    Str_English_Chinese = u'([^a-z^A-Z^ａ-ｚ^Ａ-Ｚ^^0-9^０-９^ㄅ-ㄩ^\u4E00-\u9FCC]+)'
    #Str_English_Chinese = u'([^a-z^A-Z^ａ-ｚ^Ａ-Ｚ^^0-9^０-９^\u3105-\u3129^\u4E00-\u9FCC]+)'
    #\u3105-\u3129為所有注音符號 
    #\u4E00-\u9FCC為所有中文
    strClean = re.sub(Str_English_Chinese,' ',StrIn)
    return strClean
def deleteBadWords(StrIn):
    Str_BadWords = u'([0-9]|[０-９]|[ㄅ-ㄩ]|延伸閱讀|連絡方式|電話預約|電話|營業時間|週一|週二|週三|週四|週五|週六|週日|周一|周二|周三|周四|周五|周六|\
                    |周日|假日|公休|平日|地址|粉絲團|星期|禮拜|時間限制|您或許對這些文章有興趣|造訪日期|全年無休|最後點餐|營業|AM|PM|上一篇|下一篇|\
                    |分享此文|您可能喜歡的文章|懶人包|臉書|Facebook|facebook|FB|fb|全世界便宜住宿看這兒|下載愛食記App隨時觀看|按個讚啦|喜歡我的分享嗎|\
                    |瘋台灣民宿網|官方網站|瀏覽人次|最新消息|餐廳名稱|消費時間|無圖文版|網誌|Postedonby|新鮮關注回聲|Christabelle的藝想世界部落格由製作|\
                    |也許對這些文章也有興趣|發表迴響|電子郵件|必要欄位標記|電子郵件|個人網站|輸入圖片顯示文字好證明你不是機器人|站內搜尋分類|最新動態|\
                    |並不會被公開|你的位址 |迴響名稱|用餐日期|留言|載入中|文章文章|粉絲頁|發表|每人平均價位|按個讚|推薦你閱讀|Instagram|instagram|\
                    |美食地圖|版權所有|網友回應|歡迎加入|標籤|著作權聲明|非經授權|不得轉載 )'
    strClean = re.sub(Str_BadWords,'',StrIn)
    return strClean
def EnglishFullToHalf(StrIn):
    return StrIn.replace(u'Ａ',u'A').replace(u'Ｂ',u'B').replace(u'Ｃ',u'C').replace(u'Ｄ',u'D')\
                .replace(u'Ｅ',u'E').replace(u'Ｆ',u'F').replace(u'Ｇ',u'G').replace(u'Ｈ',u'H')\
                .replace(u'Ｉ',u'I').replace(u'Ｊ',u'J').replace(u'Ｋ',u'K').replace(u'Ｌ',u'L')\
                .replace(u'Ｍ',u'M').replace(u'Ｎ',u'N').replace(u'Ｏ',u'O').replace(u'Ｐ',u'P')\
                .replace(u'Ｑ',u'Q').replace(u'Ｒ',u'R').replace(u'Ｓ',u'S').replace(u'Ｔ',u'T')\
                .replace(u'Ｕ',u'U').replace(u'Ｖ',u'V').replace(u'Ｗ',u'W').replace(u'Ｘ',u'X')\
                .replace(u'Ｙ',u'Y').replace(u'Ｚ',u'Z').replace(u'ａ',u'a').replace(u'ｂ',u'b')\
                .replace(u'ｃ',u'c').replace(u'ｄ',u'd').replace(u'ｅ',u'e').replace(u'ｆ',u'f')\
                .replace(u'ｇ',u'g').replace(u'ｈ',u'h').replace(u'ｉ',u'i').replace(u'ｊ',u'j')\
                .replace(u'ｋ',u'k').replace(u'ｌ',u'l').replace(u'ｍ',u'm').replace(u'ｎ',u'n')\
                .replace(u'ｏ',u'o').replace(u'ｐ',u'p').replace(u'ｑ',u'q').replace(u'ｒ',u'r')\
                .replace(u'ｓ',u's').replace(u'ｔ',u't').replace(u'ｕ',u'u').replace(u'ｖ',u'v')\
                .replace(u'ｗ',u'w').replace(u'ｘ',u'x').replace(u'ｙ',u'y').replace(u'ｚ',u'z')

# 移除指定tag
def removeTag(soup,tag):
    [x.extract() for x in soup.select(tag)]
# 取得文章內文
def  GetArticle(urlIn):
#     res = requests.get(urlIn, headers=headRandom)    #用手機的headers抓不到部分資料
    res = requests.get(urlIn,headers=head)
#     res = requests.get(urlIn)
    print res
#     print res.text
    res.encoding = 'utf-8'
    soup = bs(res.text, "lxml")
    removeTag(soup,'script')
    removeTag(soup,'a')
    removeTag(soup,'.rank')
    removeTag(soup,'iframe')
    removeTag(soup,'.fsb-social-bar')
    removeTag(soup,'small')
    removeTag(soup,'.comment-content.comment')                         #bearxchu
    removeTag(soup,'.moreincategories.clearfix')                       #bearxchu
    removeTag(soup,'.relativepost.clearfix')                           #bearxchu
    removeTag(soup,'.auth')                                            #bearxchu
    removeTag(soup,'.store')                                           #bearxchu
    removeTag(soup,'.comments-area')                                   #leosheng
    removeTag(soup,'.sharedaddy.sd-sharing-enabled')                   #mshw
    removeTag(soup,'.vcard')                                           #funtory
    removeTag(soup,'#facebook')                                        #alisha
    removeTag(soup,'#sidebar')                                         #alisha
    removeTag(soup,'#jp-relatedposts')                                 #nurseilife
    removeTag(soup,'.hot-info')                                        #nurseilife
    removeTag(soup,'.agoda-link')                                      #nurseilife
    removeTag(soup,'#notice')                                          #nurseilife
    removeTag(soup,'.tag')                                             #nurseilife
    
    
    xuite = soup.select('.blogbody')
    pixnet = soup.select('.article-content-inner')
    ifoodie = soup.select('#blog_content')
    miha = soup.select('#content article')                             #banbi
    itiffany = soup.select('.entry-content')                           #sflife,candicecity,mshw
    snowhy = soup.select('.page-single')                                       
    bearxchu = soup.select('.sidebar_content')
    citynotes = soup.select('.entry-content.clearfix')
    wiselyview = soup.select('.entry')
    jumpman = soup.select('.tm-article-content.uk-margin')
    jumpman2 = soup.select('.tz-row')
    amystalk = soup.select('.post-body.entry-content')
    niniblue = soup.select('#article')
    fashionguide = soup.select('#articleContent')
    ikachalife = soup.select('.post_content')
    lucida = soup.select('.single-content')


    art = xuite+pixnet+ifoodie+miha+bearxchu+citynotes+wiselyview+amystalk
    urlType = urlIn.split('/')[2]
    print urlType
    if urlType=='mshw.info' or urlType=='itiffany.cc' or urlType=='sflife.cc' :
        art = itiffany
    elif urlType=='www.alberthsieh.com':
        art = miha
    elif urlType=='lucida.cc':
        art = lucida
    #snowhy,happygululu,leosheng,    
    elif urlType=='snowhy.tw'  or urlType=='happygululu.com' or urlType=='leosheng.tw' :   
        art = snowhy
    elif urlType=='niniblue.com':
        art = niniblue
    elif urlType=='blog.fashionguide.com.tw':
        art = fashionguide
    elif urlType=='ikachalife.com':
        art = ikachalife
    elif urlType=='www.jumpman.tw':
        art = jumpman+jumpman2        
    urlType2 = urlType.split('.')[1]
    print urlType2
    if urlType2=='blogspot':
        art = amystalk
    
            
    #去除沒有內文的標籤，並將有內文的標籤去除，一筆筆加入
    line = [a.text for a in art ]
    st1 = "".join("".join(line).split()) 
    st2=retain_English_Chinese_Arabic_numerals(st1)
    st3=deleteBadWords(st2)
    st4=EnglishFullToHalf(st3)
    return st4  


def main():
#     for blog in listAllArticle[0:1]:
#          blog['article'] = GetArticle(blog['url'])
#          print blog['article']
#          print type(blog['article'])


    
    url = 'http://niniblue.pixnet.net/blog/post/218293683'
    url = 'http://shichia17.blogspot.tw/2016/05/blog-post_22.html'
    url = 'http://blog.fashionguide.com.tw/3398/posts/233392'
    url = 'http://mshw.info/mshw/?p=5380'
    
    ArticleContent=GetArticle(url)
    print ArticleContent,',',len(ArticleContent)


if __name__== "__main__":
    main()
    