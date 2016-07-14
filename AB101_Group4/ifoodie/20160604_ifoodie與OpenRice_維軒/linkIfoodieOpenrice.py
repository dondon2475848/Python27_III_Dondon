# coding=utf-8
# 使python可以讀取中文

import json
import os
import requests
import operator
import csv
import codecs  

# 創立資料夾
def mkdir(path):
    if  os.path.exists(path)==False:
        os.makedirs(path)
        print '呼叫mkdir，創立資料夾:',path    
mkdir('./log/')
def createLog(count,rid,ExceptType):
    with open('./log/%s.txt' % (ExceptType) , 'a') as f:
        f.write(str(count)+','+rid+'\n')
def encodeUtf8(dataIn):
    if dataIn is None:
        return None
    else:
        return dataIn.encode('utf-8')
        
def main():
#     with open('./data/ifoodieRestaurantDic20160524.json','r') as f:
#         RestaurantDic=json.load(f)
    #print len(RestaurantDic)
    # 共有 27912 間餐廳被收錄
    
# V1:初次跑出的餐廳字典檔
#     CityDic={}
#     for restaurant in RestaurantDic.values():
#         if restaurant['city'] not in CityDic:
#             CityDic[restaurant['city']]=1
#         elif restaurant['city'] in CityDic:
#             CityDic[restaurant['city']]+=1
#     #print CityDic
#     print json.dumps(CityDic, ensure_ascii=False)
#     mkdir('./data/restaurant/')
#     with open('./data/restaurant/ifoodieRestaurantV1.json','w') as f:
#         json.dump(CityDic,f)


    taiwanCityList = [
        u'台北市',
        u'高雄市',
        u'台中市',
        u'新北市',
        u'台南市',
        u'桃園市',
        u'新竹市',
        u'宜蘭縣',
        u'屏東縣',
        u'彰化縣',
        u'新竹縣',
        u'花蓮縣',
        u'嘉義市',
        u'苗栗縣',
        u'南投縣',
        u'基隆市',
        u'桃園縣',
        u'雲林縣',
        u'台東縣',
        u'嘉義縣',
        u'澎湖縣',
        u'金門縣',
        u'連江縣'
    ]
# V2:使用Google Api來更新
# V1→V2 非在 taiwanCityList 的城市    
#     url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&language=zh-TW'
#     CityDic={}
#     for rDic in RestaurantDic.values():
#         if rDic['city'] not in taiwanCityList:
#             if rDic['city'] not in CityDic:
#                 CityDic[rDic['city']]=1
#             elif rDic['city'] in CityDic:
#                 CityDic[rDic['city']]+=1
#     print json.dumps(CityDic, ensure_ascii=False)

# V1→V2 非在 taiwanCityList 的城市，依地址查City        
#     url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&language=zh-TW'
#     CityDic={}
#     for rDic in RestaurantDic.values():
#         if rDic['city'] not in taiwanCityList:
#             res = requests.get(url.format(rDic['address'].encode('utf-8')))
#             jd = json.loads(res.text, encoding='utf8')['results']
#             if jd !=[]:
#                 rDic['lat'] = jd[0]['geometry']['location']['lat']
#                 rDic['lng'] = jd[0]['geometry']['location']['lng']
#                 try:
#                     for i in jd[0]['address_components']:
#                         if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
#                             rDic['city'] = i['short_name']
#                             break
#                 except IndexError:
#                     pass   
#             if rDic['city'] not in CityDic:
#                 CityDic[rDic['city']]=1
#             elif rDic['city'] in CityDic:
#                 CityDic[rDic['city']]+=1
#     print json.dumps(CityDic, ensure_ascii=False)
                
# V1→V2 非在 taiwanCityList 的城市，依經緯度查City        
#     CityDic={}
#     for rDic in RestaurantDic.values():
#         if rDic['city'] not in taiwanCityList:
#             url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&language=zh-TW'
#             res = requests.get(url.format(rDic['address'].encode('utf-8')))
#             jd = json.loads(res.text, encoding='utf8')['results']
#             if jd !=[]:
#                 rDic['lat'] = jd[0]['geometry']['location']['lat']
#                 rDic['lng'] = jd[0]['geometry']['location']['lng']
#                 try:
#                     for i in jd[0]['address_components']:
#                         if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
#                             rDic['city'] = i['short_name']
#                             break
#                 except IndexError:
#                     pass   
#         
#         if rDic['city'] not in taiwanCityList:
#             url = 'http://maps.google.com/maps/api/geocode/json?latlng={0},{1}&language=zh-TW&sensor=true'
#             res = requests.get(url.format(rDic['lat'],rDic['lng']))
#             jd = json.loads(res.text, encoding='utf8')['results']
#             if jd!=[]:
#                 try:
#                     for i in jd[0]['address_components']:
#                         if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
#                             rDic['city'] = i['short_name']
#                             break
#                 except IndexError:
#                     pass     
#             
#             if rDic['city'] not in CityDic:
#                 CityDic[rDic['city']]=1
#             elif rDic['city'] in CityDic:
#                 CityDic[rDic['city']]+=1
#     print json.dumps(CityDic, ensure_ascii=False)          
        
# V2 使用Google Api來處理非在 taiwanCityList 的城市，依地址查City，依經緯度查City兩階段處理後的資料      
#     CityDic={}
#     for rDic in RestaurantDic.values():
#         if rDic['city'] not in taiwanCityList:
#             url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&language=zh-TW'
#             res = requests.get(url.format(rDic['address'].encode('utf-8')))
#             jd = json.loads(res.text, encoding='utf8')['results']
#             if jd !=[]:
#                 rDic['lat'] = jd[0]['geometry']['location']['lat']
#                 rDic['lng'] = jd[0]['geometry']['location']['lng']
#                 try:
#                     for i in jd[0]['address_components']:
#                         if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
#                             rDic['city'] = i['short_name']
#                             break
#                 except IndexError:
#                     pass   
#         
#         if rDic['city'] not in taiwanCityList:
#             url = 'http://maps.google.com/maps/api/geocode/json?latlng={0},{1}&language=zh-TW&sensor=true'
#             res = requests.get(url.format(rDic['lat'],rDic['lng']))
#             jd = json.loads(res.text, encoding='utf8')['results']
#             if jd!=[]:
#                 try:
#                     for i in jd[0]['address_components']:
#                         if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
#                             rDic['city'] = i['short_name']
#                             break
#                 except IndexError:
#                     pass     
#             
#         if rDic['city'] not in CityDic:
#             CityDic[rDic['city']]=1
#         elif rDic['city'] in CityDic:
#             CityDic[rDic['city']]+=1
#     print json.dumps(CityDic, ensure_ascii=False)     
#     mkdir('./data/')
#     with open('./data/ifoodieRestaurantDic20160606_cityUpdate.json','w') as f:
#         json.dump(RestaurantDic,f)    
    
# V2 使用Google Api來處理非在 taiwanCityList 的城市，依地址查City，依經緯度查City兩階段處理後的資料
# 印出所有餐廳所在城市，Dic
#     with open('./data/ifoodieRestaurantDic20160606_cityUpdate.json','r') as f:
#         rUpdateDic=json.load(f)
#     CityDic={}
#     for rDic in rUpdateDic.values():
#         if rDic['city'] not in taiwanCityList:
#             if rDic['city'] not in CityDic:
#                 CityDic[rDic['city']]=1
#             elif rDic['city'] in CityDic:
#                 CityDic[rDic['city']]+=1
#     print json.dumps(CityDic, ensure_ascii=False)
    
    # 將餐廳增加inTaiwan變數：0代表國外、1代表在台灣
#     with open('./data/ifoodieRestaurantDic20160606_cityUpdate.json','r') as f:
#         rOldDic=json.load(f)
#     for rDic in rOldDic.values():
#         if rDic['city'] in taiwanCityList:
#             rDic['inTaiwan']=1
#         else:
#             rDic['inTaiwan']=0
#         #print json.dumps(rDic,ensure_ascii=False)
#     with open('./data/ifoodieRestaurantDic20160606_AddinTaiwan.json','w') as f:
#         json.dump(rOldDic,f)
    # 印出只有台灣的餐廳Dic
#     with open('./data/ifoodieRestaurantDic20160606_AddinTaiwan.json','r') as f:
#         rDic=json.load(f)
#     len(rDic)
#     rNewDic={}
#     for r in rDic.values():
#         if r['inTaiwan']==1:
#             rNewDic[r['_id']]=r
#     #print json.dumps(rNewDic,ensure_ascii=False)
#     with open('./data/ifoodieRestaurantDic20160606_OnlyTaiwan.json','w') as f:
#         json.dump(rNewDic,f)
    # 印出台灣餐廳在各city的數量
    # 存只有台灣且加入OpenRice編碼的資料
    # Openrice各city的編碼
#     openRiceCityCode = {
#         u'台北市':704,
#         u'高雄市':708,
#         u'台中市':706,
#         u'新北市':705,
#         u'台南市':707,
#         u'桃園市':709,
#         u'新竹市':710,
#         u'宜蘭縣':703,
#         u'屏東縣':708,
#         u'彰化縣':711,
#         u'新竹縣':710,
#         u'花蓮縣':703,
#         u'嘉義市':712,
#         u'苗栗縣':710,
#         u'南投縣':711,
#         u'基隆市':705,
#         u'桃園縣':709,
#         u'雲林縣':712,
#         u'台東縣':703,
#         u'嘉義縣':712,
#         u'澎湖縣':703,
#         u'金門縣':703,
#         u'連江縣':703
#     }
#     with open('./data/ifoodieRestaurantDic20160606_OnlyTaiwan.json','r') as f:
#         rDic=json.load(f)
#     for u in rDic.values():
#         u['regionId']=openRiceCityCode[u['city']]
#     
#     
#     CityDic={}   
#     for r in rDic.values():
#         if r['city'] not in CityDic:
#             CityDic[r['city']]=1
#         elif r['city']  in CityDic:
#             CityDic[r['city']]+=1
#     sortedCity = sorted(CityDic.iteritems(),key=operator.itemgetter(1),reverse=True)
#     # 看一下長相
#     for c in sortedCity:
#         print openRiceCityCode[c[0]], c[0], c[1]
#     #print json.dumps(CityDic,ensure_ascii=False)
#     with open('./data/ifoodieRestaurantDic20160609_OnlyTaiwanAddOpenriceCityCode.json','w') as f:
#         json.dump(rDic,f)
    
    #Openrice的資料merge成一個資料
#     openriceDic={}
#     fileDir='./data/openrice/'
#     for fileName in os.listdir(fileDir):
#         if 'openrice' in fileName:
#             with open(fileDir+fileName,'r') as f :
#                 jd=json.load(f)
#                 for ele in jd:
#                     if ele not in openriceDic:
#                         openriceDic[ele]=jd[ele]
#     print len(openriceDic)
#     with open('./data/openriceRestaurantDic20160609.json','w') as f:
#         json.dump(openriceDic,f)
                        
    # ifoodie與openrice 取經緯度最近的餐廳
    with open('./data/openriceRestaurantDic20160609.json','r') as f:
        opDic=json.load(f)
    # ifoodie有 27791 筆餐廳資料
    with open('./data/ifoodieRestaurantDic20160609_OnlyTaiwanAddOpenriceCityCode.json','r') as f:
        iDic=json.load(f)
    
    listForCsv=[['city','regionId','address','ifoodieId','ifoodie_Restaurant_Name','openrice_Restaurant_Name','openriceId']]

    startNum=0
    EndNum=len(iDic)
    test=iDic.values()[startNum:EndNum]
    count=startNum-1

    for i in test:
        try:
            distance = {}
            for op in opDic:
                lat = opDic[op]['mapLatitude']
                lng = opDic[op]['mapLongitude']
                lat2 = (i['lat'] - lat)**2
                lng2 = (i['lng'] - lng)**2
                distance[lat2+lng2] = op
            minDistantRestaurant=distance[min(distance.keys())]
            count+=1
            #print encodeUtf8(opDic[minDistantRestaurant]['name'])
            data=[encodeUtf8(i['city']),i['regionId'],encodeUtf8(i['address']),i['_id'],encodeUtf8(i['name']),encodeUtf8(opDic[minDistantRestaurant]['name']),minDistantRestaurant]
            print count, data
    
            #print 'ifoodie name:',i['name'],'\t\t , openrice name:', opDic[minDistantRestaurant]['name']
            listForCsv.append(data)
        except:
            createLog(count,i['_id'],'Error')
    with open('./Excel/ifoodie_openrice_Restaurant.csv','wb') as f:
        f.write(codecs.BOM_UTF8)
        w = csv.writer(f, dialect='excel')
        w.writerows(listForCsv)
    print '有',EndNum-startNum,'筆餐廳資料'




if __name__== "__main__":
    main()
    