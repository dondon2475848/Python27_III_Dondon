# coding=utf-8
# 使python可以讀取中文
import json

def main():
    listNew=[]
    with open('./data/listAllArticle_New_0_10000_10000.json','r') as f:
        r_part1=json.load(f)[0:10000];
    print len(r_part1)
    with open('./data/listAllArticle_New_10000_45000_35000.json','r') as f:
        r_part2=json.load(f)[10000:45000];
    print len(r_part2)
    with open('./data/listAllArticle_New_45000_72838_27838.json','r') as f:
        r_part3=json.load(f)[45000:72838];
    print len(r_part3)
    listNew=r_part1+r_part2+r_part3
    print len(listNew)
    with open('./data/listAllArticle_New_0_72838_v1.json','w') as f:
        json.dump(listNew,f)
        
    


if __name__== "__main__":
    main()
    