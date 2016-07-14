# coding=utf-8
# 使python可以讀取中文
import json


def main():
    with open('./data/blog/article/listAllArticle_New_0_10000_10000.json','r') as f:
        listAllArticle_New_0_10000_10000 = json.load(f)
    List_0_10000 = listAllArticle_New_0_10000_10000[0:10000]
    print len(List_0_10000)
    
    with open('./data/blog/article/listAllArticle_New_10000_20000_10000.json','r') as f:
        listAllArticle_New_10000_20000_10000 = json.load(f)
    List_10000_20000 = listAllArticle_New_10000_20000_10000[10000:20000]
    print len(List_10000_20000)
    
    with open('./data/blog/article/listAllArticle_New_20000_30000_10000.json','r') as f:
        listAllArticle_New_20000_30000_10000 = json.load(f)
    List_20000_30000 = listAllArticle_New_20000_30000_10000[20000:30000]
    print len(List_20000_30000)
    
    with open('./data/blog/article/listAllArticle_New_30000_72838_42838.json','r') as f:
        listAllArticle_New_30000_72838_42838 = json.load(f)
    List_30000_72838 = listAllArticle_New_30000_72838_42838[30000:72838]
    print len(List_30000_72838)
    
    listMerge=List_0_10000+List_10000_20000+List_20000_30000+List_30000_72838
    print 'listMerge',len(listMerge)
    print 'listAllArticle_New_0_10000_10000的長度',len(listAllArticle_New_0_10000_10000)
    
    with open('./data/blog/article/listMerge_72838.json', 'w') as f:
                json.dump(listMerge, f)

if __name__== "__main__":
    main()
    