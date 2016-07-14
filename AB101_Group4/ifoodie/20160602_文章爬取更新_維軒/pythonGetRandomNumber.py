# coding=utf-8
# 使python可以讀取中文
import random
import time
import os
import json

# 建立資料夾
def mkdir(path):
    if os.path.exist(path)==False:
        os.makedirs(path)
        print '在',path,'建立資料夾'


# 取後不放回
def getRandomNumberList(getCount,minNumber,maxNumber):
    choiced = [] # 選到的號碼
    for i in range(getCount):
        choiced.append(random.choice([x for x in range(minNumber , maxNumber) if x not in choiced]))
    return choiced


def main():
    try:
        startTime=time.time()
        count=1000
        min=0
        max=72838
        ramdomNumberList = getRandomNumberList(count,min,max)
        print ramdomNumberList
        print '陣列長度為',len(ramdomNumberList)
        endTime=time.time()
        print '由',min,'到',max,'隨機抽',count,'筆，共花',endTime-startTime,'秒'
        mkdir('./data/blog/article/')
        with open('./data/blog/article/randomNumberList1000.json','w') as f:
            json.dump(ramdomNumberList,f)
    except:
        print 'Error'
       

if __name__== "__main__":
    main()
    