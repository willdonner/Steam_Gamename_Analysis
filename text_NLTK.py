import nltk
import os
import re
#from pandas import DataFrame
import pandas as pd
with open('/Users/willdonner/DevsTest/gametest.txt','r',encoding='utf-8') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='utf-8') as f:
        str1=file1.read()
        
        tokens = str(nltk.word_tokenize(str1))
        str2=re.sub("[^A-Za-z/ ]", "", tokens)
        print(str2)
        for num, line in enumerate(str2):
            if num == 2:
                print("shuchu%s"%line)
        # f.write(str2)
        # f.write(str2)
        # box=[]
        # for line in file1:
        #     box.extend(line.lower().strip().split())
        # # str2=re.sub("[^A-Za-z\ ]", "", str1)
        # # df = DataFrame(box)
        # # print(df)

        