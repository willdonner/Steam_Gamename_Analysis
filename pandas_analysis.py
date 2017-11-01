import nltk
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from numpy import *
import re
# str2=[]
istkey = []
listval = []
with open('/Users/willdonner/DevsTest/stop_words.txt','r',encoding='utf-8') as file1:
    str1 = file1.read()
    str2 = re.sub("[^A-Za-z\ ]", "", str1)
    tokenstr = nltk.word_tokenize(str2)
    fdist = nltk.FreqDist(tokenstr)
    print(u".........统计出现最多的前30个词..............")
for key, val in sorted(fdist.viewitems(), key=lambda x: (x[1], x[0]), reverse=True)[:30]:
    listkey.append(key)
    listval.append(val)
    print(key, val, u' ',)

    df = pd.DataFrame(listval, columns=[u'次数'])
    df.index = listkey
    df.plot(kind='bar')
    plt.title(u'关于steam')
    plt.savefig('3.jpg')
    plt.show()
