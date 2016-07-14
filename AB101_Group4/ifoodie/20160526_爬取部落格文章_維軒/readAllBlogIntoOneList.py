# coding=utf-8
# 使python可以讀取中文
import os
import json
# 創立資料夾的function
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path
        
def main():
   print ("main def start")
   count=0
   Path="./data/blog/"
   listTem=[]
   finalDic={}
   for filename in os.listdir(Path):
       if filename.split('_')[0]=='ifoodBlog':
           print "Loading: %s" % filename
           print '－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
           with open(Path+filename,'r') as f1:
               fileRange=filename.split('_',1)[1].replace('.json','')
               fileDic=json.load(f1)
               #PrintKeyValue(dicFile)
               fileList=fileDic['blog']
               
               
               if fileList:  #有文章才做事
                   count+=1
                   for blogDic in fileList:
                       dicTem={}
                       #PrintKeyValue(blogDic)
                       dicTem['_id']=blogDic['_id']
                       dicTem['blog_type']=blogDic['blog_type']
                       dicTem['url']=blogDic['url']
                       #dicTem['article']=GetArticle( dicTem['url'] )
                       #PrintKeyValue(dicTem)
                       listTem.append(dicTem)
   finalDic['blogContent']=listTem
   mkdir(Path+'article/')
#    with open(Path+'article/'+'finalDic'+'.json' , 'w') as f:
#        json.dump(finalDic, f)
   with open(Path+'article/'+'listTem'+'.json' , 'w') as f:
       json.dump(listTem, f)
   
   print '共有 ',count,' 個file內有文章'


if __name__== "__main__":
    main()
    