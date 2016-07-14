# coding=utf-8


import re

# 取出英文、中文
def retain_English_Chinese_Arabic_numerals(StrIn):
    Str_English_Chinese = u'([^a-z^A-Z^ａ-ｚ^Ａ-Ｚ^^0-9^０-９^ㄅ-ㄩ^\u4E00-\u9FCC]+)'
    #Str_English_Chinese = u'([^a-z^A-Z^ａ-ｚ^Ａ-Ｚ^^0-9^０-９^\u3105-\u3129^\u4E00-\u9FCC]+)'
    #\u3105-\u3129為所有注音符號 
    #\u4E00-\u9FCC為所有中文
    strClean = re.sub(Str_English_Chinese,' ',StrIn)
    return strClean
def deleteBadWords(StrIn):
    Str_BadWords = u'([0-9]|[０-９]|[ㄅ-ㄩ]|延伸閱讀|連絡方式|電話預約|電話|營業時間|週一|週二|週三|週四|週五|週六|週日|周一|周二|周三|周四|周五|周六|\
                                                        周日|假日|公休|平日|地址|粉絲團|星期|禮拜|時間限制)'
    strClean = re.sub(Str_BadWords,'',StrIn)
    return strClean
def EnglishFullToHalf(StrIn):
    return StrIn.replace(u'Ａ',u'A').replace(u'Ｂ',u'B').replace(u'Ｃ',u'C').replace(u'Ｄ',u'D')\
                .replace(u'Ｅ',u'E').replace(u'Ｆ',u'F').replace(u'Ｇ',u'G').replace(u'Ｈ',u'H')\
                .replace(u'Ｉ',u'I').replace(u'Ｊ',u'J').replace(u'Ｋ',u'K').replace(u'Ｌ',u'L')\
                .replace(u'Ｍ',u'M').replace(u'Ｎ',u'N').replace(u'Ｏ',u'O').replace(u'Ｐ',u'P')\
                .replace(u'Ｑ',u'Q').replace(u'Ｒ',u'R').replace(u'Ｓ',u'S').replace(u'Ｔ',u'T')\
                .replace(u'Ｕ',u'U').replace(u'Ｖ',u'V').replace(u'Ｗ',u'W').replace(u'Ｘ',u'X')\
                .replace(u'Ｙ',u'Y').replace(u'Ｚ',u'Z').replace(u'ａ',u'a').replace(u'ｂ',u'b')\
                .replace(u'ｃ',u'c').replace(u'ｄ',u'd').replace(u'ｅ',u'e').replace(u'ｆ',u'f')\
                .replace(u'ｇ',u'g').replace(u'ｈ',u'h').replace(u'ｉ',u'i').replace(u'ｊ',u'j')\
                .replace(u'ｋ',u'k').replace(u'ｌ',u'l').replace(u'ｍ',u'm').replace(u'ｎ',u'n')\
                .replace(u'ｏ',u'o').replace(u'ｐ',u'p').replace(u'ｑ',u'q').replace(u'ｒ',u'r')\
                .replace(u'ｓ',u's').replace(u'ｔ',u't').replace(u'ｕ',u'u').replace(u'ｖ',u'v')\
                .replace(u'ｗ',u'w').replace(u'ｘ',u'x').replace(u'ｙ',u'y').replace(u'ｚ',u'z')


str=u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,\
ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ,\
0123456789０１２３４５６７８９,\
,.，。﹝﹞\
時間宅咚咚時間限制周一\
ㄅㄆㄇㄧㄨㄩ\
'
print retain_English_Chinese_Arabic_numerals(str)
print deleteBadWords(retain_English_Chinese_Arabic_numerals(str))
print '============================================================'
print EnglishFullToHalf(deleteBadWords(retain_English_Chinese_Arabic_numerals(str)))