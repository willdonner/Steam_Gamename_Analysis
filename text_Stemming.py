import os
import re
from nltk.stem.lancaster import LancasterStemmer
import nltk
word_box =[]
box = []
with open('/Users/willdonner/DevsTest/result1.txt','r',encoding='utf-8') as file1:
    with open('/Users/willdonner/DevsTest/stemm.txt','w',encoding='utf-8') as f:
        str_read = file1.read()
        word_box.extend(nltk.word_tokenize(str_read))
        stemm = LancasterStemmer()
        for stemm_word in word_box:  
            # print(stemm.stem(word_box))
        #f.write(str1)
            #  print (stemm_word,stemm.stem(stemm_word))
            #  f.write(stemm.stem(stemm_word))
             box.append(stemm.stem(stemm_word))
        str1 = str(box)
        f.write(str1)
        # print("q")

        # words =['fishing', 'crying', 'likes', 'meant', 'owed','wars', 'did', 'done', 'women',"avaliable"]
        # for word in words:
        #     print (word,stemm.stem(word))