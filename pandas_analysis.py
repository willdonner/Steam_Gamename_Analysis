import nltk
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from numpy import *
import re
from pyecharts import Bar
from pyecharts import Page
from pyecharts import Bar3D
from pyecharts import Pie
# str2=[]
listkey = []
listval = []

with open('/Users/willdonner/DevsTest/result2.txt','r',encoding='utf-8') as file1:
    str1 = file1.read()
    str2 = re.sub("[^A-Za-z\ ]", "", str1)
    tokenstr = nltk.word_tokenize(str2)
    fdist = nltk.FreqDist(tokenstr)

    print(u".........统计出现最多的前30个词..............")
for key, val in sorted(fdist.items(), key=lambda x:(x[1],x[0]),reverse=True)[:10]:
    listkey.append(key)
    listval.append(val)
    print(key,val,u' ')

page = Page()
df = pd.DataFrame(listval,columns=[u'count'])
df.index = listkey
attr1 = listkey
v11 = listval
bar = Bar("Bar - datazoom - top20")
bar.add("", attr1, v11, is_datazoom_show=True, datazoom_type='both', datazoom_range=[10,20])
page.add(bar)

bar3d = Bar3D("3D 柱状图", width=1200, height=600)
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [
    [0, 0, 5]
    ]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3d_width=200, grid3d_depth=80)
page.add(bar3d)

pie = Pie("饼图", title_pos='center')
pie.add("", attr1, v11, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
page.add(pie)
page.render()
# df.plot(kind='bar')
# plt.show()
