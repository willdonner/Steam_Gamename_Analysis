# 2017-10-24 by willdonner
# 统计文本量 主要用于查找 是否多余过滤（手动...
import os
line_count = 0
words_count = 0
char_count = 0
with open('/Users/willdonner/DevsTest/result1.txt','r',encoding='latin-1') as file1:
    for line in file1:
        words = line.split()
        line_count+=1
        words_count+=len(words)
        char_count+=len(line)

    print("line_count",line_count)
    print("words_count",words_count)
    print("char_count",char_count)