#2017-10-26 by willdonner
#使用regexp 模块 并设置最小处理长度是6
import os
import re
from nltk.stem.regexp import RegexpStemmer
import nltk
import collections
word_box =[]
box = []
collect_box = []
with open('/Users/willdonner/DevsTest/result1.txt','r',encoding='utf-8') as file1:
    with open('/Users/willdonner/DevsTest/stemm.txt','w',encoding='utf-8') as f:
        str_read = file1.read()
        str1 = re.sub("[^A-Za-z\ ]", "", str_read)
        word_box.extend(nltk.word_tokenize(str1))
        stemm = RegexpStemmer('ing$|s$|ables$',min=6)
        for stemm_word in word_box:  
            if re.match(r'[A-Za-z]',stemm_word):
            # print(stemm.stem(word_box))
        #f.write(str1)
                # print (stemm_word,stemm.stem(stemm_word))
            #  f.write(stemm.stem(stemm_word))
             box.append(stemm.stem(stemm_word))
        collect_box = collections.Counter(box)
        str1 = str(collect_box)
        f.write(str1)
        # print("q")

        # words =['fishing', 'crying', 'likes', 'meant', 'owed','wars', 'did', 'done', 'women',"avaliable"]
        # for word in words:
        #     print (word,stemm.stem(word))