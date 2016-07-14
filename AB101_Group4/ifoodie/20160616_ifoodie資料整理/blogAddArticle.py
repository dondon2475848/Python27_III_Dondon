# coding=utf-8
# 使python可以讀取中文
import json
import os
import time
import csv

# 創立資料夾
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path  

def main():
    starTime=time.time()
    blogNoArticleList=[['author_id','blog_id','blogUrl']]
    with open('./data/dataOut/ifoodieBlogDic20160524AddAuthor_id.json' , 'r') as f:
        blogDic=json.load(f)
    with open('./data/blogArticle/listAllArticle_New_0_72838_v12.json' , 'r') as f:
        blogArticleList=json.load(f)

        for blogArticleDic in blogArticleList:
            try:
                blogDic[blogArticleDic['_id']]['article']=blogArticleDic['article']  
            except KeyError:
                blogNoArticleMessage=[blogDic[blogArticleDic['_id']]['author_id'],blogArticleDic['_id'],blogArticleDic['url']]
                blogNoArticleList.append(blogNoArticleMessage)
                blogDic[blogArticleDic['_id']]['article']=[]
            except :
                print 'Fail!!'
    
    # 將文章內容為[]的資料令存成csv檔
    mkdir('./Excel/')  
    with open('./Excel/blogNoArticle_V12.csv','wb') as f:
        w = csv.writer(f)
        w.writerows(blogNoArticleList)   
    with open('./data/dataOut/ifoodieBlogDic20160616Author_id_Article.json','w') as f:
        json.dump(blogDic,f)    
    endTime=time.time()
    print '共花',endTime-starTime,'秒'

if __name__== "__main__":
    main()
    