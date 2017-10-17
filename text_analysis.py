import collections
import os

# From_file= open('/Users/willdonner/DevsTest/game_urls.txt','r',encoding='UTF-8')
# f= open ('/Users/willdonner/DevsTest/game_urls1.txt','w',encoding='UTF-8')
# count=0
# for each_line in From_file:
#     f.writelines(each_line+',')
#     count+=1
#     # f.close()
#     # From_file.close()
#     print('文件中总共有：%d行'%count)
with open('/Users/willdonner/DevsTest/game_urls.txt','r',encoding='UTF-8') as file1:
    str1=file1.read().split(' ')
    print("原文本:%s"%str1)
    print("处理后的:%s"%collections.Counter(str1))