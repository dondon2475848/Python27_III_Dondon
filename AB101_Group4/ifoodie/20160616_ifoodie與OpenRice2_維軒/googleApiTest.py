# coding=utf-8
# 使python可以讀取中文
import json 
import requests



def main():
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&language=zh-TW'

    res = requests.get(url.format(u'高雄市楠梓區楠梓新路369號'.encode('utf-8')))
    jd = json.loads(res.text, encoding='utf8')['results']
    print json.dumps(jd,ensure_ascii=False)
    print jd[0]['geometry']['location']['lat']
    print jd[0]['geometry']['location']['lng']
     


if __name__== "__main__":
    main()
    