# coding=utf-8
# 使python可以讀取中文
import json
import os

def encodeUtf8(dataIn):
    if dataIn is None:
        return None
    else:
        return dataIn.encode('utf-8')

def main():
    with open('./data/ifoodieRestaurantDic20160616_UpdategoogleLatLng_v2.json','r') as f:
        ifDic=json.load(f)
    #print len(ifDic) # 27791
    
    with open('./data/openriceRestaurantDic20160609.json','r') as f:
        orDic=json.load(f)
    #print len(orDic) # 91822
    
    startNum=0
    EmdNum=1
    indexCount=startNum-1
    for ifR in ifDic.values()[startNum:EmdNum]:
        distance = {}
        for orR in orDic:
            lat = orDic[orR]['mapLatitude']
            lng = orDic[orR]['mapLongitude']
            lat2 = (ifR['lat'] - lat)**2
            lng2 = (ifR['lng'] - lng)**2
            distance[(lat2+lng2)**0.5] = orR
        minDistantRestaurant=distance[min(distance.keys())]
        print type(minDistantRestaurant)
        indexCount+=1
        #print encodeUtf8(opDic[minDistantRestaurant]['name'])
        data=[encodeUtf8(ifR['city']),ifR['regionId'],encodeUtf8(ifR['address']),ifR['_id'],encodeUtf8(ifR['name'])\
              ,encodeUtf8(orDic[minDistantRestaurant]['name']),minDistantRestaurant,distance[minDistantRestaurant]]
        print indexCount,',', json.dumps(data, encoding='UTF-8', ensure_ascii=False)

        #print 'ifoodie name:',i['name'],'\t\t , openrice name:', opDic[minDistantRestaurant]['name']
        #listForCsv.append(data)
    

if __name__== "__main__":
    main()
    