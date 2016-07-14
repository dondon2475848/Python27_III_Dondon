# coding=utf-8
# 使python可以讀取中文

### import part
import os
import json
import re
import requests
from bs4 import BeautifulSoup as bs




### def part:
# 創立資料夾的function
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path
# 印出字典的key與value
def PrintKeyValue(dic_in):
    for key, value in dic_in.iteritems() :
        #print key,'\t', value
        print '|' , key.ljust(25) ,'|' , value  
    print '－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
# 輸出錯誤訊息 
def createLog(log, type1):
    date = time.strftime('%Y%m%d')
    with open('./data/log/%s_%s.txt' % (type1, date), 'a') as f:
        f.write(log+'\n')
    exceptCount+=1
# 取出英文、中文
def retain_English_Chinese(StrIn):
    Str_English_Chinese = u'([^a-z^A-Z^\uFF21-\uFF3A^\uFF41-\uFF5A^\u4E00-\u9FCC]+)'
    # uFF21為全型A  uFF3A為全型Z  uFF41為全型a  uFF5A為全型z   
    #u4E00為中文的第一個字：一 u9FCC為中文的最後一個字
    strClean = re.sub(Str_English_Chinese,' ',StrIn)
    return strClean
# 刪除不需要的詞彙
def deleteBadWords(StrIn):
    Str_BadWords = u'(延伸閱讀|連絡方式|電話預約|電話|營業時間|週一|週二|週三|週四|週五|週六|週日|周一|周二|周三|周四|周五|周六|\
                                                        周日|假日|公休|平日|地址|粉絲團|星期|禮拜|時間限制)'
    strClean = re.sub(Str_BadWords,'',StrIn)
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
   print ("main def start")
   count=0
   Path="./data/small_Data_0_589/blog/"
   for filename in os.listdir(Path):
       if filename.split('_')[0]=='ifoodBlog':
           print "Loading: %s" % filename
           print '－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
           with open(Path+filename,'r') as f1:
               fileRange=filename.split('_',1)[1].replace('.json','')
               fileDic=json.load(f1)
               #PrintKeyValue(dicFile)
               fileList=fileDic['blog']
               listTem=[]
               
               if fileList:  #有文章才做事
                   count+=1
                   for blogDic in fileList:
                       dicTem={}
                       #PrintKeyValue(blogDic)
                       dicTem['_id']=blogDic['_id']
                       dicTem['blog_type']=blogDic['blog_type']
                       dicTem['url']=blogDic['url']
                       dicTem['article']=GetArticle( dicTem['url'] )
                       #PrintKeyValue(dicTem)
                       listTem.append(dicTem)
                   mkdir(Path+'article/')
                   with open(Path+'article/'+'listAddArticle'+fileRange+'.json' , 'w') as f2:
                       json.dump(listTem, f2)
   
   print '共有 ',count,' 個file內有文章'



if __name__== "__main__":
    main()
    
    
    
