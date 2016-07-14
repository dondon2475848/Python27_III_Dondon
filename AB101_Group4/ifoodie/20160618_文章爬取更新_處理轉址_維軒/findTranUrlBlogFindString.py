# coding=utf-8
# 使python可以讀取中文
import json
import re

def main():

    with open('./data/blogListNeedDealWith.json','r') as f:
        moveList=json.load(f);
    print len(moveList)
    count=0
    for bL in moveList.values():
        if re.search(u'我搬家了', bL['article']):
            count+=1
    print count


        
    


if __name__== "__main__":
    main()
    