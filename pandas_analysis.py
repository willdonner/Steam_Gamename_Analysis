import nltk
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from numpy import *
import re
from pyecharts import Bar

# str2=[]
listkey = []
listval = []

with open('/Users/willdonner/DevsTest/result2.txt','r',encoding='utf-8') as file1:
    str1 = file1.read()
    str2 = re.sub("[^A-Za-z\ ]", "", str1)
    tokenstr = nltk.word_tokenize(str2)
    fdist = nltk.FreqDist(tokenstr)

    print(u".........统计出现最多的前30个词..............")
for key, val in sorted(fdist.items(), key=lambda x:(x[1],x[0]),reverse=True)[:20]:
    listkey.append(key)
    listval.append(val)
    print(key,val,u' ')

df = pd.DataFrame(listval,columns=[u'count'])
df.index = listkey
attr = listkey
v1 = listval
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.render()

attr1 = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v11 = [5, 20, 36, 10, 75, 90]
v21 = [10, 25, 8, 60, 20, 80]
bar1 = Bar("柱状图数据堆叠示例")
bar1.add("商家A", attr1, v11, is_stack=True)
bar1.add("商家B", attr1, v21, is_stack=True)
bar1.render()
# df.plot(kind='bar')
# plt.show()
