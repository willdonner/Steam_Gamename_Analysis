import nltk
import os
import re
from pandas import DataFrame
import pandas as pd
with open('/Users/willdonner/DevsTest/ys.txt','r',encoding='GBK') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='GBK') as f:
        box=[]
        for line in file1:
            box.extend(line.strip().split())
        # str2=re.sub("[^A-Za-z\ ]", "", str1)
        df = DataFrame(box)
        print(df)
        