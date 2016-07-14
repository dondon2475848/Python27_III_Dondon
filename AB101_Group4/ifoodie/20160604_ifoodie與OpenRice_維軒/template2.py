# coding=utf-8
# 使python可以讀取中文

def main():
    word = 'abcdefg'
    trie = {}  
    p = trie  
    for c in word:   
        p[c] = {}  
        p = p[c]
    print p
    print trie


if __name__== "__main__":
    main()
    