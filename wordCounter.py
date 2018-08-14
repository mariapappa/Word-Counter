# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 22:44:16 2018

@author: Maria
"""
from io import open
import collections
import chardet
import sys 

reload(sys)
sys.setdefaultencoding('utf8')

file = open('short-story.txt')
a = file.read()

# detect file encoding
with open('short-story.txt', 'rb') as file:
    raw = file.read(32) # at most 32 bytes are returned
    encoding = chardet.detect(raw)['encoding']

with open('short-story.txt', encoding=encoding) as file:
    text = file.read()

wordcount = {}

for word in text.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("*","")
    word = word.replace("//","")
    word = word.replace("/","")
    word = word.replace("--","")
    word = word.replace(")","")
    word = word.replace("(","")
    word = word.replace("]","")
    word = word.replace("[","")
    word = word.replace("#","")
    word = word.replace("?","")
    word = word.replace("'","")
    word = word.replace(";","")
    word = word.replace("_","")
    word = word.replace("\\", "/")
    word = word.replace("-", "")
    word = word.replace("$", "")
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

text_file = open('Output.txt','w')

word_counter = collections.Counter(wordcount)


for word, count in word_counter.most_common(len(word_counter)):
    text_file.write("%s : %d \n" % (unicode(word),count))
    
# Close the file
file.close()
text_file.close()
