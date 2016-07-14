# coding=utf-8
# 使python可以讀取中文
import json
import csv
import time

# Variable
date = time.strftime('%Y%m%d')

# Def
# 輸出錯誤訊息 
def createLog(listIndex,blog_id,blog_url,ExceptType):
    with open('./data/log/ArticleLenLess100_1_%s_%s_v20160619.txt' %(date,ExceptType) , 'a') as f:
        f.write(str(listIndex)+','+blog_id+','+blog_url+'\n')
def main():
    with open('./data/ifoodieBlogDic20160619Update5PixnetSmallEnglish.json','r') as f:
        listMerge_72838 = json.load(f)
    indexCount=-1
    ArticleLenLess100 =0
    ArticleLenLess100List=[['index','blogIdAtIfoodie','articleLength','blogUrl']]
    for blog in listMerge_72838.values():
        indexCount+=1
        data=[]
        try:
            if len(blog['article'])<100:
                ArticleLenLess100 += 1
                data=[indexCount,blog['_id'],len(blog['article']),blog['url']]
                ArticleLenLess100List.append(data)
                print indexCount,blog['_id'],',',len(blog['article']),',',blog['url']
        except KeyError:
            createLog(indexCount,blog['_id'],blog['url'],'KeyError')
        except: 
            createLog(indexCount,blog['_id'],blog['url'],'OtherError')
    # 將文章內容不到100字的文字存成CSV檔
    with open('./Excel/ArticleLenLess100_Report_v20160619.csv','wb') as f:
        w = csv.writer(f)
        w.writerows(ArticleLenLess100List)
        
    print '有',ArticleLenLess100,'個字典內文章內容小於100'
                  

if __name__== "__main__":
    main()
    