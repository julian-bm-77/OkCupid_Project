'''
Template for OkCupid
'''


import matplotlib.pyplot as plt
import wordcloud as wc
import re
import pandas as pd
import numpy as np

def csv_to_df(filename):
    ''' Function: csv_to_df
        Parameters: filename (string), header (list)
        Returns: dataframe containing information from
                the file and headers from input
    '''

    df = pd.read_csv(filename) #,names = header)
    return df

def read_txt(text):
    ''' Function: read_txt
        Parameters: name of speech file (string)
        Returns: the text (string) but with punctuation, 
            square brackets, and weird line breaks removed
    '''

    text = re.sub('\[.+\]','',text)
    text = re.sub('\<.+\>','',text)
    text = re.sub('[^\w\s]','',text)
    text = re.sub('href','',text) #my attempt at removing added linebreaks (temporary)
    text = re.sub('br','',text) #my attempt at removing added linebreaks (temporary)
    
    return text

def generate_wc(name,text):
    ''' Function: generate_wc
        Parameters: name (string), text (string)
        Returns: nothing, just creates a wordcloud with the most popular words in a president's speech. 
    '''
    cloud = wc.WordCloud().generate(text)
    plt.imshow(cloud)
    plt.axis('off')
    plt.title(name)
    plt.show()

def combine_essay0(df):
    ''' Function: combine
        Parameters: dataframe
        Returns: string of all essay0 responses combined
    '''
    essay = list(df.essay0)
    essay = [str(i) for i in essay]
    texts = ' '.join(essay)
    texts = read_txt(texts)
    return(texts)

if __name__ == "__main__":
    okcupid = 'profiles.csv.zip'
    df = csv_to_df(okcupid)
    df.dropna(inplace=True)
    texts = combine_essay0(df)
    generate_wc('essay0',texts)