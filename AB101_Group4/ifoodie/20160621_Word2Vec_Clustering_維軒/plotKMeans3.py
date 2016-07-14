# coding=utf-8
# 使python可以讀取中文


#data
import gensim
import logging
import json

from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
# The Old Faithful data set is a set of historical observations showing the waiting time before an eruption aThe Old Faithful data set is a set of historical observations showing the waiting time before an eruption and the length of the eruption. In the last post we looked into it a littlnd the length of the eruption. In the last post we looked into it a littl
model = gensim.models.Word2Vec.load('./data/Doc2Vec_Size_100_1_m_new')
# KMean前處理
# 詞清單
wordlist = model.index2word
# 詞向量
wordVector = model.syn0
wordVectorShape=wordVector.shape[0]
print  wordVectorShape
# num_clusters = wordVectorShape/ 5
# print num_clusters


import time

start = time.time() # Start time

# Set "k" (num_clusters) to be 1/5th of the vocabulary size, or an
# average of 5 words per cluster


data = model.syn0
num_clusters = 3


# now with K = 3 (3 clusters)
centroids,_ = kmeans(data,num_clusters)
idx,_ = vq(data,centroids)

plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or',
     data[idx==2,0],data[idx==2,1],'og') # third cluster points
plot(centroids[:,0],centroids[:,1],'sm',markersize=3)
show()

end = time.time()
elapsed = end - start
print "Time taken for K Means clustering: ", elapsed, "seconds."


print 'Finish'