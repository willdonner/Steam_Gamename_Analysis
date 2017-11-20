import nltk
import os
import re
from nltk.corpus import stopwords
import text_count
#from pandas import DataFrame
#import pandas as pd
# 使用了简单的NLTK的停用词库
# 不能满足要求 还需要自定义
word_box =[]
box=[]
with open('/Users/willdonner/DevsTest/gameall/19vgsales.csv','r',encoding='latin-1') as file1:
    with open('/Users/willdonner/DevsTest/gameall/result2.txt','w+',encoding='utf-8') as f:
        str1=file1.read().lower()
        word_box.extend(nltk.word_tokenize(str1))
        # tokens = (nltk.word_tokenize(str1))
        english_punctuation_letter = ['a','b','c','d','e','f','g','h','i','j','k','l'
        ,'m','n','o','p','q','r','s','t','u','v','w','x','y','z','/']
        english_punctuation = ['addon','add-on','demo','dlc','edition','ground','grounds','original','pack','rocksmith','rocksmithâ®','simulator'
        ,'soundtrack','vr','character','collector','game','ii','ost','remastered','rpg','set','song','steam','train'
        ,'bundle','deluxe','episode','fsx','maker','official','puzzle','season','skin','token','ultimate','add'
        ,'beta','chapter','from','ii','ix','my','online','viii','x','awesomenaut','br','digital','hd','iii','iv'
        ,'one','pfrpg','ts','vol','vx','3d','complete','costume','demon','expansion','part','pro','tailer','vi'
        ,'new','vii','skin','ost','present','fantasy','class','loco','two','/']
        english_word_stop = set(stopwords.words('english'))
        for i in word_box:
            if re.match(r'[A-Za-z]',i):
                if i not in english_word_stop:
                    if i not in english_punctuation_letter:
                        if i not in english_punctuation:
                            box.append(i)
        str3 = str(box)
        str2=re.sub("[^A-Za-z/ ]", "", str3)
            #print(str2)
            # for num, line in enumerate(str2):
            #     if num == 0:
            #         print("输出%s"%line)
        f.write(str3)
        text_c = text_count.text_counts()
        text_c.print_count(box)
        
        # f.write(str2) 
#使用pandas分析数据
        # box=[]
        # for line in file1:
        #     box.extend(line.lower().strip().split())
        # # str2=re.sub("[^A-Za-z\ ]", "", str1)
        # # df = DataFrame(box)
        # # print(df)

        