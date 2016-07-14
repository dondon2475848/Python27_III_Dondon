# coding=utf-8
# 使python可以讀取中文
import requests
import json
import time
import os
import Levenshtein
from fuzzywuzzy import fuzz


def main():
    ifName   ='梁記麻辣火鍋冰棒豆腐'
    
    orName   ='桔園'
    orName2  ='火鍋冰棒豆腐'
    orName3  ='梁記'
    orName4  ='梁記麻辣火鍋'
    orName5  ='梁記石頭火鍋'
    orName6  ='梁記火鍋'
    
    
    print  'jaro'
    print  orName,':',Levenshtein.jaro(ifName, orName)
    print  orName2,':',Levenshtein.jaro(ifName, orName2)
    print  orName3,':',Levenshtein.jaro(ifName, orName3)
    print  orName4,':',Levenshtein.jaro(ifName, orName4)
    print  orName5,':',Levenshtein.jaro(ifName, orName5)
    print  orName6,':',Levenshtein.jaro(ifName, orName6)
    
    
    print  '---------------------------'
    print  'jaro_winkler'
    print  orName,':',Levenshtein.jaro_winkler(ifName, orName, 0.25)
    print  orName2,':',Levenshtein.jaro_winkler(ifName, orName2, 0.25)
    print  orName3,':',Levenshtein.jaro_winkler(ifName, orName3, 0.25)
    print  orName4,':',Levenshtein.jaro_winkler(ifName, orName4, 0.25)
    print  orName5,':',Levenshtein.jaro_winkler(ifName, orName5, 0.25)
    print  orName6,':',Levenshtein.jaro_winkler(ifName, orName6, 0.25)
    print  '---------------------------'
    print  'distance'
    print  orName,':',Levenshtein.distance(ifName, orName)
    print  orName2,':',Levenshtein.distance(ifName, orName2)
    print  orName3,':',Levenshtein.distance(ifName, orName3)
    print  orName4,':',Levenshtein.distance(ifName, orName4)
    print  orName5,':',Levenshtein.distance(ifName, orName5)
    print  orName6,':',Levenshtein.distance(ifName, orName6)
    print  '---------------------------'
    print  'ratio'
    print  orName,':',Levenshtein.ratio(ifName, orName)
    print  orName2,':',Levenshtein.ratio(ifName, orName2)
    print  orName3,':',Levenshtein.ratio(ifName, orName3)
    print  orName4,':',Levenshtein.ratio(ifName, orName4)
    print  orName5,':',Levenshtein.ratio(ifName, orName5)
    print  orName6,':',Levenshtein.ratio(ifName, orName6)
    print  '---------------------------'
    print  'fuzzywuzzyRatio'
    print  orName,':',fuzz.ratio(ifName, orName)
    print  orName2,':',fuzz.ratio(ifName, orName2)
    print  orName3,':',fuzz.ratio(ifName, orName3)
    print  orName4,':',fuzz.ratio(ifName, orName4)
    print  orName5,':',fuzz.ratio(ifName, orName5)
    print  orName6,':',fuzz.ratio(ifName, orName6)
    print  '---------------------------'
    print  'fuzzywuzzyPartial_ratio'
    print  orName,':',fuzz.partial_ratio(ifName, orName)
    print  orName2,':',fuzz.partial_ratio(ifName, orName2)
    print  orName3,':',fuzz.partial_ratio(ifName, orName3)
    print  orName4,':',fuzz.partial_ratio(ifName, orName4)
    print  orName5,':',fuzz.partial_ratio(ifName, orName5)
    print  orName6,':',fuzz.partial_ratio(ifName, orName6)
    print  '---------------------------'
    print  'fuzzywuzzyToken_sort_ratio'
    print  orName,':',fuzz.token_sort_ratio(ifName, orName)
    print  orName2,':',fuzz.token_sort_ratio(ifName, orName2)
    print  orName3,':',fuzz.token_sort_ratio(ifName, orName3)
    print  orName4,':',fuzz.token_sort_ratio(ifName, orName4)
    print  orName5,':',fuzz.token_sort_ratio(ifName, orName5)
    print  orName6,':',fuzz.token_sort_ratio(ifName, orName6)
    print  '---------------------------'
    print  'fuzzywuzzyToken_set_ratio'
    print  orName,':',fuzz.token_set_ratio(ifName, orName)
    print  orName2,':',fuzz.token_set_ratio(ifName, orName2)
    print  orName3,':',fuzz.token_set_ratio(ifName, orName3)
    print  orName4,':',fuzz.token_set_ratio(ifName, orName4)
    print  orName5,':',fuzz.token_set_ratio(ifName, orName5)
    print  orName6,':',fuzz.token_set_ratio(ifName, orName6)





    
    

if __name__== "__main__":
    main()
    