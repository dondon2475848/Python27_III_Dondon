# coding=utf-8
# 使python可以讀取中文
import json
def main():
#    Str1 = "abcd  咚咚"
#    print Str1
#    print len(Str1)
    with open('./data/blog/article/listMerge_72838.json','r') as f:
        listMerge_72838 = json.load(f)
    for blog in listMerge_72838:
        if len(blog['article'])<100:
            print blog['_id'],',',len(blog['article']),',',blog['url']


if __name__== "__main__":
    main()
    