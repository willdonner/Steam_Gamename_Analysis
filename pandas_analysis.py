
import os
import matplotlib.pyplot as plt
import pandas as pd
str2=[]
with open('/Users/willdonner/DevsTest/stop_words.txt','r+',encoding='utf-8') as file1:
    str1 = file1.read()
    str2.extend(str1)
    df = pd.DataFrame(str2,columns=[u'次数'])
    df.index = str2
    df.plot(kind ='bar')
    plot.title('title')
    plot.show()
    

