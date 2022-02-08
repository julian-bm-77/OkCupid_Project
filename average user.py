#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:52:55 2021

@author: juliann
"""

import matplotlib.pyplot as plt
from statistics import mode
from math import floor
import pandas as pd


        
    
def average_user(data, sex):
    # creating integeres to average out data 
    age_sum = 0
    smokes_sum = 0
    drinks_sum = 0
    height_sum = 0
    gender_count = 0
    genders = []
    for i in data.index:
        if data.loc[i]['sex'] == sex:
            gender_count += 1
            #adding quantitative data to a total to be average out
            height_sum += data.loc[i]['height']
            age_sum += data.loc[i]['age']
            genders.append(data.loc[i]['sex'])
            #quantifying data that's qualitative
            if data.loc[i]['smokes'] == 'when drinking':
                smokes_sum += 1
            elif data.loc[i]['smokes'] == 'sometimes':
                smokes_sum += 2
            elif data.loc[i]['smokes'] == 'yes':
                smokes_sum += 3
            elif data.loc[i]['smokes'] == 'trying to quit':
                smokes_sum += 4
            if data.loc[i]['drinks'] == 'rarely':
                drinks_sum += 1
            elif data.loc[i]['drinks'] == 'socially':
                drinks_sum += 2
            elif data.loc[i]['drinks'] == 'often':
                drinks_sum += 3
            elif data.loc[i]['drinks'] == 'desperately':
                drinks_sum += 4
    # creating averages of all the totals so far
    average_age = age_sum / gender_count
    average_smokes = smokes_sum / gender_count
    average_drinks = drinks_sum / gender_count
    average_height = height_sum / gender_count
    # average out height, with feet and inches
    inches = average_height % 12
    feet = floor(average_height/12)
    average_gender = mode(genders)
    # printing out the average person, with the chosen gender as a parameter
    print('average gender: ', str(average_gender))
    print('average age: ', str(average_age))
    print('average drinking amount: ', str(average_drinks))
    print('average smoking amount: ', str(average_smokes))
    print('average height: ', str(feet), '\' ', str(inches), '\"')
    



    
def open(filename):
    ''' Function: get_jsonfile
        Parameters: filename, a string (JSON file), plus a list of fields
                    we care about
        Returns: a dictionary of points
    '''
    #CREATING OKCUPID DATAFRAME FROM CSV
    data = pd.read_csv(filename)

    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data

data = open('profiles.csv.zip')
 

if __name__ == "__main__":
    # opening the data into a dataframe
    okcupid_data = open('profiles.csv.zip')
    # creating the average male and female
    average_user(okcupid_data, 'm')
    average_user(okcupid_data, 'f')
    
    
    
