#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:18:35 2021

@author: manonledonne
"""

import pandas as pd 
from textblob import TextBlob

def sentiment(value):
    if type(value) == str:
        return TextBlob(value).sentiment.polarity
    else:
        return None

pf = pd.read_csv("profiles.csv", usecols=["sex", "essay0"])


pf["sentiment"] = pf["essay0"].apply(lambda value: sentiment(value))

average = pf.groupby(["sex"]).mean("sentiment")

print(average)


