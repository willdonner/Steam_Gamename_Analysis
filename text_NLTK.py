import nltk
import os
import re
from nltk.corpus import stopwords
#from pandas import DataFrame
#import pandas as pd
word_box =[]
box=[]
with open('/Users/willdonner/DevsTest/game_urls.csv','r',encoding='latin-1') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='utf-8') as f:
        str1=file1.read().lower()
        word_box.extend(nltk.word_tokenize(str1))
        # tokens = (nltk.word_tokenize(str1))
        english_word_stop = set(stopwords.words('english'))
        for i in word_box:
            if i not in english_word_stop:
                box.append(i)
        str3 = str(box)
        str2=re.sub("[^A-Za-z/ ]", "", str3)
        #print(str2)
        # for num, line in enumerate(str2):
        #     if num == 0:
        #         print("输出%s"%line)
        f.write(str2)
        # f.write(str2) 
#使用pandas分析数据
        # box=[]
        # for line in file1:
        #     box.extend(line.lower().strip().split())
        # # str2=re.sub("[^A-Za-z\ ]", "", str1)
        # # df = DataFrame(box)
        # # print(df)

        