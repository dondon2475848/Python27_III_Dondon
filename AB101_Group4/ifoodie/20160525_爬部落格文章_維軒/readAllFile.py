# coding=utf-8
# 使python可以讀取中文
import os
DATA_DIR = "./data/small_Data_0_589/blog/"
file_data = []
for filename in os.listdir(DATA_DIR):
    # print "Loading: %s" % filename
    print DATA_DIR,filename
