import collections
import os
import re

def get_words(file):  
    with open (file) as f:  
        words_box=[]  
        for line in f:                           
                if re.match(r'[a-zA-Z0-9]',line):  
                    words_box.extend(line.strip().split())                 
    return collections.Counter(words_box)  
a=get_words('/Users/willdonner/DevsTest/emma.txt')
print(a.most_common(10))  
# 格式化文本在每一行数据后添加一个‘,’分隔符
From_file= open('/Users/willdonner/DevsTest/game_urls.txt','r',encoding='UTF-8')
f= open ('/Users/willdonner/DevsTest/game_urls1.txt','w',encoding='UTF-8')
count=0
for each_line in From_file:
    f.writelines(each_line+',')
    count+=1
    # f.close()
    # From_file.close()
    print('文件中总共有：%d行'%count)

#用python自带的collections库做简单的文本分析和频率统计
box1=[]
words_box=[]
with open('/Users/willdonner/DevsTest/stemm.txt','r',encoding='UTF-8') as file1:
    with open('/Users/willdonner/DevsTest/result.txt','w',encoding='UTF-8') as f:
        str1 = file1.read()
        for line in str1:
            if re.match(r'[A-Za-z]',line):
                words_box.extend(line.lower().strip().split()) 
                box1 = collections.Counter(words_box)
                str2 = str(words_box)
        #str3 = re.sub("[^A-Za-z\ ]", "", str2)
        f.write("处理后的:%s"%box1)
        str2=file1.read().strip(' ')
        str1=str(re.sub("[^A-Za-z]", "", str2))
        f.write("处理后的:%s"%collections.Counter(str2))
        str2=file1.read().split(' ')
        f.write("处理后的:%s"%str2)
        str1=re.sub("[^A-Za-z\,\'\[\]\"\]", "", str2)
        f.write("处理后的:%s"%str1)
        print("原文本:%s"%str1)
        print("处理后的:%s"%collections.Counter(str1))
with open('/Users/willdonner/DevsTest/result.txt','w',encoding='UTF-8') as f:
    f.close()
