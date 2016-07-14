# coding=utf-8
# 使python可以讀取中文
import csv
def main():
    data = [
            ['a','b','c'],
            [1,2,3],
            [4,5,6]
           ]
    f = open("csvTest.csv","wb")
    w = csv.writer(f)
    w.writerows(data)
    f.close()

 

if __name__== "__main__":
    main()
    