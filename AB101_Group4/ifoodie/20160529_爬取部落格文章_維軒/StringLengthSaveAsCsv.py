# coding=utf-8
# 使python可以讀取中文
import json
import csv
# 輸出錯誤訊息 
def createLog(listIndex,blog_id,blog_url,ExceptType):
    with open('./data/blog/article/log/ArticleLenLess100_1_%s_log.txt' %(ExceptType) , 'a') as f:
        f.write(str(listIndex)+','+blog_id+','+blog_url+'\n')
def main():
    with open('./data/blog/article/listMerge_72838.json','r') as f:
        listMerge_72838 = json.load(f)
    indexCount=-1
    ArticleLenLess100List=[['index','blogIdAtIfoodie','articleLength','blogUrl']]
    for blog in listMerge_72838:
        indexCount+=1
        data=[]
        try:
            if len(blog['article'])<100:
                data=[indexCount,blog['_id'],len(blog['article']),blog['url']]
                ArticleLenLess100List.append(data)
                print indexCount,blog['_id'],',',len(blog['article']),',',blog['url']
        except:
            createLog(indexCount,blog['_id'],blog['url'],'NoArticle')
            
    f = open("./data/blog/article/log/ArticleLenLess100_1.csv","wb")
    w = csv.writer(f)
    w.writerows(ArticleLenLess100List)
    f.close()        

if __name__== "__main__":
    main()
    