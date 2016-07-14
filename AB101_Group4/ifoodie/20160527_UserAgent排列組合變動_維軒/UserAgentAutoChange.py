# coding=utf-8
# 使python可以讀取中文
import random

head = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; H30-L02 Build/HonorH30-L02) \
AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36"
}
brand=['HTC','Sony','Asus','Acer','Samsung','LG','Motorola','InFocus','GSmart','OPPO','TWM','OKWAP','HUAWEI']
model=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
head2 = {
"User-Agent": "Mozilla/5.0 (Linux; Android 4.{0}.{1};{2} {3}{4}-{5}{6}) \
AppleWebKit/537.36 (KHTML, like Gecko) Version/{7}.0 Chrome/30.0.0.0 Mobile Safari/537.36"\
.format(random.randint(0,9),random.randint(0,9),brand[random.randint(0,len(brand)-1)],\
model[random.randint(0,len(model)-1)],random.randint(1,99),model[random.randint(0,len(model)-1)],\
random.randint(799,1599),random.randint(250,9999))
}


def b():
    print 'template'
def main():
   with open('./data/blog/article/listAllArticle.json','r') as f:
        listAllArticle = json.load(f)
   


if __name__== "__main__":
    main()
    