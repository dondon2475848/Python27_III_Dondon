
# coding: utf-8

# # 整理資料

# In[1]:

#整理資料
import os
import re
import json
import time
import requests
import math

#讀資料去除重複並加入索引
def readData(path,key):
    data = {}
    for fname in os.listdir(path):
        if re.search('.*ifood.*',fname):
            with open(path+'/'+fname, 'r') as f:
                jd = json.load(f)[key]
                for ele in jd:
                    if ele['_id'] not in data:
                        data[ele['_id']] = ele
                    elif ele['timestamp'] > data[ele['_id']]['timestamp']:
                        data[ele['_id']] = ele
    return data


path = '/Users/fan/PycharmProjects/ETL/IFOOD/{}'
user = readData(path.format('user'), 'user')
blog = readData(path.format('blog'), 'blog')
restaurant = readData(path.format('restaurant'), 'restaurant')
# 統計域名
typeDict = {}
for b in blog.values():
    if b['blog_type'] not in typeDict:
        typeDict[b['blog_type']] = 1
    else:
        typeDict[b['blog_type']] += 1
# 去除pixnet
noPixnet = [ele for ele in typeDict.keys() if 'pixnet' not in ele]
#for domain in noPixnet:
#    print domain

# 排除自推，計算每個人喜歡特定人文章的數量
def countAuthor(dict, user, blog, collection):
    for bg in user[collection]:
        if bg in blog and blog[bg]['author_id'] not in like and blog[bg]['author_id'] != user['_id']:
            dict[blog[bg]['author_id']] = 1
        elif bg in blog and blog[bg]['author_id'] in like and blog[bg]['author_id'] != user['_id']:
            dict[blog[bg]['author_id']] += 1
    return dict

# 填入author
for u in user:
    for bg in user[u]['blog_id_list']:
        if blog[bg]:
            blog[bg]['author_id'] = u
        else:
            blog[bg]['author_id'] = None

# 計算喜歡次數            
for us in user:
    like = {}
    try:
        like = countAuthor(like, user[us], blog, 'collection_blog_list')
        like = countAuthor(like, user[us], blog, 'recommendation_blog_list')
        user[us]['like'] = like
    except KeyError:
        user[us]['like'] ={}
print len(user)
print len(blog)
print len(restaurant)

normalcity = [
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


# # 檢查分佈

# In[2]:

#檢查分佈
import operator
city = {}
for r in restaurant.values():
    if r['city'] not in city:
        city[r['city']] = 1
    else:
        city[r['city']] += 1
sortedCity = sorted(city.iteritems(),key=operator.itemgetter(1),reverse=True)
for c in sortedCity:
    print c[0], c[1]


# # 依地址查城市

# In[3]:

normalcity = [
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
url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&language=zh-TW'
for r in restaurant.values():
    if r['city'] not in normalcity:
        res = requests.get(url.format(r['address'].encode('utf-8')))
        jd = json.loads(res.text, encoding='utf8')['results']
        if jd:
            r['lat'] = jd[0]['geometry']['location']['lat']
            r['lng'] = jd[0]['geometry']['location']['lng']
            try:
                for i in jd[0]['address_components']:
                    if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
                        r['city'] = i['short_name']
                        break
            except IndexError:
                pass     


# # 依經緯度查城市

# In[4]:

url = 'http://maps.google.com/maps/api/geocode/json?latlng={},{}&language=zh-TW&sensor=true'
for r in restaurant.values():
    if r['city'] not in normalcity:
        res = requests.get(url.format(r['lat'],r['lng']))
        jd = json.loads(res.text, encoding='utf8')['results']
        if jd:
            try:
                for i in jd[0]['address_components']:
                    if i['types'][0] == 'administrative_area_level_2' or i['types'][0] == 'administrative_area_level_1':
                        r['city'] = i['short_name']
                        break
            except IndexError:
                pass


# # 將英文轉為中文

# In[6]:

temp = [
    'Taipei City',
    'Kaohsiung City',
    'Taichung City',
    'New Taipei City',
    'Tainan City',
    'Taoyuan City',
    'Hsinchu City',
    'Yilan County',
    'Pingtung County',
    'Changhua County',
    'Hsinchu County',
    'Hualien County',
    'Chiayi City',
    'Miaoli County',
    'Nantou County',
    'Keelung City',
    'Taoyuan City',
    'Yunlin County',
    'Taitung County',
    'Chiayi County',
    'Penghu County',
    'Kinmen County',
    'Lianjiang '  
]

cc = [
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

engToChn = dict((k,v) for k,v in zip(temp,cc))
for r in restaurant.values():
    if r['city'] in temp:
        r['city'] = engToChn[r['city']]


# # 再次檢查分佈

# In[7]:

#檢查分佈
import operator
city = {}
for r in restaurant.values():
    if r['city'] not in city:
        city[r['city']] = 1
    else:
        city[r['city']] += 1
sortedCity = sorted(city.iteritems(),key=operator.itemgetter(1),reverse=True)
for c in sortedCity:
    print c[0], c[1]


# # 留下台灣的餐廳並插入openrice的城市編號

# In[12]:

restaurantInTaiwan =[restaurant[r] for r in restaurant if restaurant[r]['city'] in normalcity]
# openrice的城市編號
cityDict = {
    'taipei':704,
    'newtaipei-keelung':705,
    'taoyuan':709,
    'hsinchu-miaoli':710,
    'taichung':706,
    'changhua-nantou':711,
    'yunlin-chiayi':712,
    'tainan':707,
    'kaohsiung-pingtung':708,
    'eastern':703,
}
# ifoodie與openrice的對照
finalCity = {
    u'台北市':704,
    u'高雄市':708,
    u'台中市':706,
    u'新北市':705,
    u'台南市':707,
    u'桃園市':709,
    u'新竹市':710,
    u'宜蘭縣':703,
    u'屏東縣':708,
    u'彰化縣':711,
    u'新竹縣':710,
    u'花蓮縣':703,
    u'嘉義市':712,
    u'苗栗縣':710,
    u'南投縣':711,
    u'基隆市':705,
    u'桃園縣':709,
    u'雲林縣':712,
    u'台東縣':703,
    u'嘉義縣':712,
    u'澎湖縣':703,
    u'金門縣':703,
    u'連江縣':703
}
# 將openrice的城市編號插入
for u in restaurantInTaiwan:
    u['regionId'] = finalCity[u['city']]
 
city = {}
for r in restaurantInTaiwan:
    if r['city'] not in city:
        city[r['city']] = 1
    else:
        city[r['city']] += 1
sortedCity = sorted(city.iteritems(),key=operator.itemgetter(1),reverse=True)
# 看一下長相
for c in sortedCity:
    print finalCity[c[0]], c[0], c[1]


# # 用ifoodie的餐廳經緯度去openrice搜尋

# In[13]:

# Authorization要換成新的才能用
head = {
    'User-Agent':'OpenRice_iOS/5.3.2 (iPhone; iOS 9.3.1)',
    'Authorization':' Bearer l4zrpGJRBQPbtzAv6JKQpLLJPr-Nju0SOf8w6W5V9nl1XmfZ6cPBQnDeHe9GZ04583CMfqBlr0KaOaVBsWnHnlxGQk79plfiQe23r1hdz4KaIKW7iKghYrL_7rcf3H_ZQIt3kNI84Hvdc3jJRQN1ryLyE-ZuxeV_rIB38jB3-76dqtir6YaECkK8cTcMZdrrPHWB30-JhliS8ipq2iZdVx2e-E6hQ0UunMDMZEPHt8r5ON3njGv898-8eObSTkXUo_XsYRGR5WtzchFVUDwojTqgKIwsS8CtABYaW9qJ01SN9yu_mH8lzXi0mbWft6MGIFN4-K1CrH1TQgcOk5MkONpE4RbL0rszslBi1p4i-4tzM6dKpgnuX8q9MO37aVr6JDFLeL02v3kK3DWrg6OcCLtpUTaGcZeErbUf_r02xPeQDPVIjPZjXSIOTwZSe6Fn_5wZhEYrLbmn8uZBNwBlCDox-pvDgV6Sz9MLGsDqzopZocLQZwRv9pmVAqV_6AxAqXLuXIOwNpHaY-VB_Yrl-mvkTkqvYwNc3qJhe8u0JzHhzu5a9Z6WvpJ_UfFO0CYiqKxXOQ'
}  
url = 'https://api-tw.openrice.com/api/v3/search?geo=wgs84%2C{}%2C{}%2Cwgs84&regionId={}&rows=100&sortBy=Distance&startAt=0&suggestedCoupon=true&withinDistance=1'

openriceList = []
page = int(math.ceil(len(restaurantInTaiwan)/100.0))
for i in xrange(0,page):
    shortDict = {}
    start = i*100
    if (i+1)*100 > len(restaurantInTaiwan):
        end = len(restaurantInTaiwan)%100 + start
    else:
        end = (i+1)*100
    for u in restaurantInTaiwan[start:end]:
        try:
            res = requests.get(url.format(u['lat'],u['lng'],u['regionId']), headers=head)
            jd = json.loads(res.text, encoding='utf8')['paginationResult']['results']
            print u['name'], 'good'
            for r in jd:
                if r['poiId'] not in openriceList:
                    openriceList.append(r['poiId'])
                    shortDict[r['poiId']] = r
        except:
            print u['name'], 'bad'
            with open('./Workspace/data/openrice/log/log.txt', 'a') as f:
                f.write(u['_id']+'\n')
    with open('./Workspace/data/openrice/openrice%d.json' % end, 'w') as f:
        json.dump(shortDict,f)


# # 讀取openrice資料

# In[11]:

data = {}
for fname in os.listdir('./Workspace/data/openrice'):
    if 'openrice' in fname:
        with open('./Workspace/data/openrice'+'/'+fname, 'r') as f:
            jd = json.load(f)
            for ele in jd:
                if ele not in data:
                    data[ele] = jd[ele]
print len(data)


# # 測試經緯度比對

# In[26]:

test = restaurantInTaiwan[0:200]
for u in test:
    distance = {}
    for op in data:
        lat = data[op]['mapLatitude']
        lng = data[op]['mapLongitude']
        lat2 = (u['lat'] - lat)**2
        lng2 = (u['lng'] - lng)**2
        distance[lat2+lng2] = op
    print u['name'], data[distance[min(distance.keys())]]['name']


# In[32]:

# openrice餐廳名、地址
simpleData = {}
for u in data:
    simpleData[u] = data[u]['name'] + '|' + data[u]['address']
with open('./Workspace/data/openriceName.json', 'w') as f:
    json.dump(simpleData,f)


# In[46]:

# ifoodie餐廳名、地址
ifoodData = {}
for u in restaurantInTaiwan:
    ifoodData[u['_id']] = '%s|%s' %(u['name'] ,u['address'])
with open('./Workspace/data/ifoodName.json', 'w') as f:
    json.dump(ifoodData,f)


# In[ ]:



