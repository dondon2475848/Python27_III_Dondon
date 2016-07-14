# coding=utf-8
# 使python可以讀取中文


import os
import json
import re
import time


# 創立資料夾
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path  
# 抓取資料夾內的json檔
def dicMerge(dataFromDir,dataOut,key):
    dicCollect = {}
    for fileName in os.listdir(dataFromDir):
        jsonList=[]
        if re.search('ifood*',fileName):
            with open (dataFromDir+fileName,'r') as f:
                jsonList=json.load(f)[key]
                for jsonDic in jsonList:
                    if jsonDic['_id'] not in dicCollect:
                        dicCollect[jsonDic['_id']]=jsonDic
                    elif jsonDic['_id'] in dicCollect and jsonDic['timestamp']>dicCollect[jsonDic['_id']]['timestamp'] :
                        dicCollect[jsonDic['_id']]=jsonDic
                    jsonDic={}
    print key,'字典的長度為',len(dicCollect)
    with open(dataOut,'w') as f:
        json.dump(dicCollect,f)    
        
def main():
    starTime=time.time()
    mkdir('./data/dataOut/')
    #dicMerge('./data/user/','./data/dataOut/ifoodieUserDic20160524.json','user')
    # 字典長度為 294634，共花 51.3329999447 秒
    #dicMerge('./data/blog/','./data/dataOut/ifoodieBlogDic20160524.json','blog')
    # 字典長度為 72838，共花 6.57500004768 秒
    #dicMerge('./data/restaurant/','./data/dataOut/ifoodieRestaurantDic20160524.json','restaurant')
    # 字典長度為 27912 ，共花 61.6459999084 秒
    endTime=time.time()
    print '共花',endTime-starTime,'秒'

if __name__== "__main__":
    main()
    