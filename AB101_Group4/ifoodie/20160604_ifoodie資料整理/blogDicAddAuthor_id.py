# coding=utf-8
# 使python可以讀取中文
import json
import time


def main():
    starTime=time.time()
    print 'Strat!'
    # 讀檔：使用者清單，已預先抓好，約29萬筆
    with open('./data/dataOut/ifoodieUserDic20160524.json','r') as f:
        UserDic = json.load(f)
    with open('./data/dataOut/ifoodieBlogDic20160524.json','r') as f:
        blogDicOld = json.load(f)    
    
    for u in UserDic:
        for blogId in UserDic[u]['blog_id_list']:
            try:
                blogDicOld[blogId]['author_id']=u
            except:
                print '沒有收入文章id為',blogId,'的文章'
    with open('./data/dataOut/ifoodieBlogDic20160524AddAuthor_id.json','w') as f:
        json.dump(blogDicOld,f)
    endTime=time.time()
    print '共花',endTime-starTime,'秒'
if __name__== "__main__":
    main()
    