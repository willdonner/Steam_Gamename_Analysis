import os
import collections
import re

with open('/Users/willdonner/DevsTest/gametest.txt','r',encoding='UTF-8') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='UTF-8') as f:
        # lines = (line.strip(',') for line in file1)
        # for line in lines:
        # for line in file1:
        str1=file1.read().strip(" ")
        str2=re.sub("[^A-Za-z/ /of]", "", str1)
        f.write(str2)