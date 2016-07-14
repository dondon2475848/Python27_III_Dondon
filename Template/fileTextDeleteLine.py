# coding=utf-8
# 使python可以讀取中文
import re

def main():
#     with open('dic.txt','r') as f:
#         for line in f.readlines():
#             if not re.search(';', line, flags=0):
#                 with open('dic2.txt','a') as f2:
#                     f2.write(line)
    with open('dic3.txt','a') as f2:                
        with open('dic.txt','r') as f:
            for line in f.readlines():
                if ';' not in line :
                    f2.write(line)         
    
    
    

if __name__== "__main__":
    main()
    