# coding=utf-8
# 使python可以讀取中文
import gensim
import logging
import json

with open ('./data/subject.json','r') as f:
	jd=json.load(f)
print json.dumps(jd.values()[0:10],ensure_ascii=False).encode('utf-8')
print len(jd)


