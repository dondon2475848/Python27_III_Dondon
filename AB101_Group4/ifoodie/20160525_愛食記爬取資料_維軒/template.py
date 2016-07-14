# coding=utf-8
# 使python可以讀取中文

import requests 
import json

head = {
        "User-Agent": "HTC AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36"
}

res = requests.get('https://ifoodie.tw/api/user/?limit=15000&offset=300', headers=head)
# jd = json.loads(res.text, encoding='utf8')
# print jd
print res.text