import os
import collections
import re
with open('/Users/willdonner/DevsTest/ys.txt','r',encoding='GBK') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='GBK') as f:
        # lines = (line.strip(',') for line in file1)
        # for line in lines:
        # for line in file1:
        str1=file1.read()
        str2=re.sub("[^A-Za-z\ ]", "", str1)
        #str3 = re.sub("[(?!the).*$]","",str2)
        f.write(str2)