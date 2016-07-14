# coding=utf-8
# 使python可以讀取中文
import random

def main():
   choiced = [] # 選到的號碼
   for i in range(11):
       choiced.append(random.choice([x for x in range(1, 12) if x not in choiced]))
   print choiced
       

if __name__== "__main__":
    main()
    