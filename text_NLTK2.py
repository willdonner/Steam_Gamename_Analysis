import nltk
import os
import re
from nltk.tokenize import word_tokenize
from collections import Counter
import collections
from nltk.text import Text
import csv
box = []
words_box = []
with open('/Users/willdonner/DevsTest/ys.txt','r',encoding='utf-8') as file1:
    with open('/Users/willdonner/DevsTest/result1.txt','w',encoding='utf-8') as f:
        gametxt = file1.read()
        box.extend(gametxt.lower().strip().split())
        words_box = collections.Counter(box)
        str1 = str(words_box)
        # for i in reader:
        #     words_box.extend(word_tokenize(i))
        # for line in gametxt:
        #     words_box.extend(line.lower().strip().split())
        # words_lower = gametxt.lower()
        #words_text = Text(words_lower)
        #tokens = str(nltk.word_tokenize(gametxt))
        # words_counter = str(Counter(tokens))
        #print(words_box[0:10])
        print(str1)