# coding=utf-8
# 使python可以讀取中文
import json

def main():
    with open('./data/ifoodieBlogDic20160619Update5Pixnet.json','r') as f:
        ifDic=json.load(f);
    print len(ifDic)
    indexCount=-1
    for b in ifDic.values():
        indexCount+=1
        print 'Index : ',',',indexCount
        if b['article'] is not None:
            smallArticle = b['article'].lower()
            b['article']=smallArticle
    
    with open('./data/ifoodieBlogDic20160619Update5PixnetSmallEnglish.json','w') as f:
        json.dump(ifDic,f)

    
        
    


if __name__== "__main__":
    main()
    