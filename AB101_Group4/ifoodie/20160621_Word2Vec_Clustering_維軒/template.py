# coding=utf-8
# 使python可以讀取中文
import gensim
import logging
import json

model = gensim.models.Word2Vec.load('./mymodelSG')


# 相似度


# for ele in model.most_similar(u'漢堡', topn=10):
#     print ele[0].encode('utf-8') ,ele[1]


# print json.dumps(model.most_similar(u'漢堡', topn=10),ensure_ascii=False).encode('utf-8')


# print model.index2word(topn=10)


# KMean前處理
# 詞清單
wordlist = model.index2word
print type(wordlist)
print json.dumps(wordlist[0:20],ensure_ascii=False).encode('utf-8') 
# 詞向量
wordvector = model.syn0
# print type(wordvector)