# coding=utf-8
# 使python可以讀取中文
import time
import sys


def main():
    date = time.strftime('%Y%m%d_%H:%M')
    print date
    
    try:
        print 1+'a'
    except:
        print sys.exc_info()[0]
        print type(str(sys.exc_info()[0]))

if __name__== "__main__":
    main()
    