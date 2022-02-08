#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:36:11 2021

@author: manonledonne
"""
import re
import pandas as pd 
from wordcloud import WordCloud
import matplotlib.pyplot as plt


essayColnames = ["essay{}".format(i) for i in range(10)]


pf = pd.read_csv("profiles.csv", usecols=essayColnames )

freq = {}
for essay in pf.essay0:
    if  type(essay) == str:
        wordList = re.sub("[^\w]"," ",essay).split()
        for word in wordList:
            if len(word)  < 9:
                continue
            if word in freq:
                freq[word] +=1
            else:
                freq[word] = 1

wordCloud = WordCloud().generate_from_frequencies(freq)

plt.title("Word Cloud Plot of essay prompts (minimum 9 letters)")
plt.axis('off')
plt.imshow(wordCloud)
   
       