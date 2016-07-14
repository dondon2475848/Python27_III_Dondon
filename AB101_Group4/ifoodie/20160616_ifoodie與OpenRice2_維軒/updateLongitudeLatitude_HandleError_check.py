# coding=utf-8
# 使python可以讀取中文
import json
import requests
import time
import sys
import os
import random

brand=['HTC','Sony','Asus','Acer','Samsung','LG','Motorola','InFocus','GSmart','OPPO','TWM','OKWAP','HUAWEI']
model=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

headRandom = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 4.{0}.{1};{2} {3}{4}-{5}{6}) \
    AppleWebKit/537.36 (KHTML, like Gecko) Version/{7}.0 Chrome/30.0.0.0 Mobile Safari/537.36"\
    .format(random.randint(0,9),random.randint(0,9),brand[random.randint(0,len(brand)-1)],\
    model[random.randint(0,len(model)-1)],random.randint(1,99),model[random.randint(0,len(model)-1)],\
    random.randint(799,1599),random.randint(250,9999))
}



def createLog(path,exceptType,errorId,listIndex):
    with open(path , 'a') as f:
        nowTime = time.strftime('%Y%m%d_%H:%M:%S')
        f.write(str(listIndex)+','+exceptType+','+errorId+','+nowTime+'\n')
# 創立資料夾的function
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path

def main():
    startTime = time.strftime('%Y%m%d_%H_%M_%S')
    ### Ifoodie的經緯度處理
    with open('./data/ifoodieRestaurantDic20160616_UpdategoogleLatLng_v2.json','r') as f:
        ifDic=json.load(f)
    print len(ifDic) #Ifoodie有27791間餐廳
    
    # 檢查ifoodie的餐廳是否皆有地址與經度(longitude)緯度(latitude)
    cDic={}
    listIndex=-1
    for rDic in ifDic.values():
        try:
            listIndex+=1
            print listIndex
            #print json.dumps(rDic,ensure_ascii=False)
            if rDic['address'] is None:
                if 'noAddress' not in cDic:
                    cDic['noAddress']=1
                else:
                    cDic['noAddress']+=1
            if rDic['googleLat'] is None:
                if 'noLat' not in cDic:
                    cDic['noLat']=1
                else:
                    cDic['noLat']+=1
            if rDic['googleLng'] is None:
                if 'nolng' not in cDic:
                    cDic['nolng']=1
                else:
                    cDic['nolng']+=1
            if rDic['googleLatLng'] ==0:
                if 'nogoogleLatLng' not in cDic:
                    cDic['nogoogleLatLng']=1
                else:
                    cDic['nogoogleLatLng']+=1
        except :
                exceptType=str(sys.exc_info()[0])
                mkdir('./data/log/')
                createLog('./data/log/%s_%s.txt' % ('updateError',startTime),exceptType,rDic['_id'],listIndex)

    print json.dumps(cDic,ensure_ascii=False)
    # {"nogoogleLatLng": 26957, "noAddress": 19}


                

if __name__== "__main__":
    main()
    