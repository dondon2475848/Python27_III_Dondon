# coding=utf-8
# 使python可以讀取中文

import os
import json
import re
import requests
from bs4 import BeautifulSoup as bs
import random
import time
import copy


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
# 印出字典的key與value
def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        print key,'  :  ', value 
# 創立資料夾
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path        
# 輸出錯誤訊息 
def createLog(blog_id,blog_url,startIndex,endIndex,listIndex,ExceptType):
    with open('./data/blog/article/log/%s_%d_%d.txt' % (ExceptType,startIndex,endIndex) , 'a') as f:
        f.write(listIndex+','+blog_id+','+blog_url+'\n')

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
    #print res
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
    amystalk = soup.select('.post-body.entry-content')
    niniblue = soup.select('#article')
    fashionguide = soup.select('#articleContent')
    ikachalife = soup.select('.post_content')


    art = xuite+pixnet+ifoodie+miha+bearxchu+citynotes+wiselyview+jumpman+amystalk
    urlType = urlIn.split('/')[2]
    print urlType
    if urlType=='mshw.info' or urlType=='itiffany.cc' or urlType=='sflife.cc' :
        art = itiffany
    elif urlType=='www.alberthsieh.com':
        art = miha
    #snowhy,happygululu,leosheng,    
    elif urlType=='snowhy.tw'  or urlType=='happygululu.com' or urlType=='leosheng.tw' :   
        art = snowhy
    elif urlType=='niniblue.com':
        art = niniblue
    elif urlType=='blog.fashionguide.com.tw':
        art = fashionguide
    elif urlType=='ikachalife.com':
        art = ikachalife
            
    urlType2 = urlType.split('.')[1]
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
    time_start_to_grab=time.time()
    mkdir('./data/blog/article/log')
    # 讀檔：使用者清單，已預先抓好，約29萬筆
    with open('./data/blog/article/listAllArticle.json','r') as f:
        listAllArticle_Old = json.load(f)
    startIndex = 30000
    endIndex   = 40000
    save_count = 1000
    
    listAllArticle_New=copy.deepcopy(listAllArticle_Old)
    ArticleLenLess100=0
    GetArticleErrorCount=0
    listIndex=startIndex-1
    count = 0
    fileCountLoop=0
    for blog in listAllArticle_New[startIndex:endIndex]:
        count += 1
        listIndex+=1
        try:
            if blog['article']:
                 if len(blog['article'])<100:
                     createLog(blog['_id'],blog['url'],startIndex,endIndex,listIndex,'ArticleLenLess100')
                     ArticleLenLess100+=1
                 continue
        except:
             try:
                blog['article'] = GetArticle(blog['url'])
                #print blog['article']
                if len(blog['article'])<100:
                    createLog(blog['_id'],blog['url'],startIndex,endIndex,listIndex,'ArticleLenLess100')
                    ArticleLenLess100+=1
                nowUseTime =time.time() - time_start_to_grab
                print '目前的List Index為',listIndex,',文章內容小於100的文章有',ArticleLenLess100,',GetArticleError的有',GetArticleErrorCount,',目前花了',nowUseTime,'秒'
             except:
                createLog(blog['_id'],blog['url'],startIndex,endIndex,'GetArticleError')
                GetArticleErrorCount+=1
        #每 save_count 筆存一次
        if count%save_count==0:
            fileCountLoop += 1
            with open('./data/blog/article/listAllArticle_New_%d_%d_%d.json' % (startIndex, endIndex,fileCountLoop*save_count), 'w') as f:
                json.dump(listAllArticle_New, f)
            
             
             
                 
    
    time_end_to_grab = time.time()
    print '總共花了 ',time_end_to_grab - time_start_to_grab,' 秒' 
    print '有',ArticleLenLess100,'個字典內文章內容小於100'
    print '有',GetArticleErrorCount,'個文章無法取得內容'
    print 'listAllArticle_New的長度為',len(listAllArticle_New)
    print 'listAllArticle_Old的長度為',len(listAllArticle_Old)
    #PrintKeyValue(listAllArticle_New[3])


if __name__== "__main__":
    main()
    