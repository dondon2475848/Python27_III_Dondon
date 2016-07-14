# coding=utf-8
# 使python可以讀取中文
import json

def main():
    listNew=[]
    with open('./data/movelist.json','r') as f:
        movelist=json.load(f);
    print len(movelist)
    for blogDic in movelist:
        #sharonwhite.pixnet.net
        if blogDic['author_id']=='55b61f2f699b6e12be3f941b':
            listNew.append(blogDic)
        #americangod.pixnet.net
        if blogDic['author_id']=='54e41f9a2756dd560a9c0203':
            listNew.append(blogDic)
        #banbi217.pixnet.net
        if blogDic['author_id']=='53bdf3bdd4fdab213072997b':
            listNew.append(blogDic)   
        #lillian1101.pixnet.net 
        if blogDic['author_id']=='55b8c4e8699b6e786a342077':
            listNew.append(blogDic) 
        #elvagwan3.pixnet.net
        if blogDic['author_id']=='54b74b42d4fdab15f36ab713':
            listNew.append(blogDic)   
    print len(listNew)
    bDic={}
    for b in listNew:
        bDic[b['_id']]=b
    
    print len(bDic)
    
    with open('./data/blogListNeedDealWith.json','w') as f:
        json.dump(bDic,f)
        

        
    


if __name__== "__main__":
    main()
    