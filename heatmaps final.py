#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:52:13 2021

@author: juliann
"""



import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


def graph_clusters(data, keepers):
    """ Function: graph_clusters
        Parameters: dtaframe of clusters, where centroids is a column
        Returns: nothing, just renders the plot
    """
    
   
    # aligning number of instances with each possible coordinate combination
    data = align_quantities(data)
    plt.figure()
    # pivoting the data for the heatmap
    heatmap1_data = pd.pivot_table(data, values= 'amount', index= keepers[1], columns=keepers[0])
    # creating and visualizing the heatmap
    sns.heatmap(heatmap1_data, cmap="Spectral")
    plt.show()
    



def align_quantities(data):
    # creating lists of the possible results for each attribute
    x = dot_size_lists(data)[0]
    y = dot_size_lists(data)[1]
    
    # determines the value of the heatmap cells
    # (counts up the number of times each possible comibations occurs)
    df = dot_size(data, x ,y)
    # turns the resultling dataframe into a list
    df = df.values.tolist()
    # taking all the results from all combinations and putting the into a list
    lst = []
    for i in df:
        lst += i
    # creating lists of x values y times, and y values x times
    # this is for the creation of a dataframe who's indeces represent coordinate combinations
    ys = y * len(x)
    xs = []
    for i in x:
        for j in y:
            xs.append(i)
    # creating a dictionary of the newly created data
    dd = {keepers[0]: ys, keepers[1]: xs, 'amount': lst}
    # turning it into a dataframe to be graphed as a heatmap
    d = pd.DataFrame(dd, columns=dd.keys())
    return d
        
    
def dot_size_lists(data):
    # creating lists to list all the possible OkCupid user inputs for the two chosen attribuets
    xs = []
    ys = []
    for i in data.index:
        # 0 and 1 are the only columns, represnting the two chosen attributes
        if data.loc[i][0] not in xs:
            xs.append(data.loc[i][0])
        if data.loc[i][1] not in ys:
            ys.append(data.loc[i][1])
    # sorting them by numeric order
    xs.sort()
    ys.sort()
    return xs, ys
    

def dot_size(data, xs, ys):
    # creating a new dataframe based off the lists of possible attribute responses
    df2 = pd.DataFrame(index = xs, columns =ys)
    for x in xs:
        for y in ys:
            # setting each cell to zero to be tallied up
            # the reaon it is set to x - 1 is because it was creating the dataframe one index forward, and this was the best solution
            # for certain attributes like age, it had to be set to [x - 18]
            df2.iloc[x -1][y] = 0
            # iterating through each user and checking if their input matches the current cell being tallied up
            for i in data.index:
                if data.iloc[i][0] == x and data.iloc[i][1] == y:
                    # if it matches, it adds one to the selected sell of the heatmap, adding 1 to the 
                    # tally of total users at this coordinate pair
                    df2.iloc[x -1][y] += 1
    return df2
    

def open_file(data):
    ''' Function: get_jsonfile
        Parameters: filename, a string (JSON file), plus a list of fields
                    we care about
        Returns: a dictionary of points
    '''
    


    #CREATING OKCUPID DATAFRAME FROM CSV
    data = pd.read_csv(data)

    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data


def get_points(data, keepers):
    ''' Function: get_jsonfile
        Parameters: filename, a string (JSON file), plus a list of fields
                    we care about
        Returns: a dictionary of points
    '''
    # creating lists for the numeric values for quantifed attributes
    orient_nums = []
    status_nums = []
    drinks_nums = []
    smokes_nums = []
    body_nums = []
    

    
    # quantifying different attributes for graphing

    for i in data.index:
        # orientation
        if data.loc[i]['orientation'] == 'straight':
            orient_nums.append(0)
        if data.loc[i]['orientation'] == 'bisexual':
            orient_nums.append(3)
        if data.loc[i]['orientation'] == 'gay':
            orient_nums.append(6)
        
        # status
        if data.loc[i]['status'] == 'single':
            status_nums.append(1)
        if data.loc[i]['status'] == 'seeing someone':
            status_nums.append(3)
        if data.loc[i]['status'] == 'available':
            status_nums.append(2)
        if data.loc[i]['status'] == 'married':
            status_nums.append(4)
        
        # drinks
        if data.iloc[i]['drinks'] == 'not at all':
            drinks_nums.append(1)
        if data.iloc[i]['drinks'] == 'rarely':
            drinks_nums.append(2)
        if data.iloc[i]['drinks'] == 'socially':
            drinks_nums.append(3)
        if data.iloc[i]['drinks'] == 'often':
            drinks_nums.append(4)
        if data.iloc[i]['drinks'] == 'very often':
            drinks_nums.append(5)
        if data.iloc[i]['drinks'] == 'desperately':
            drinks_nums.append(6)
        
        # smokes
        if data.iloc[i]['smokes'] == 'no':
            smokes_nums.append(1)
        if data.iloc[i]['smokes'] == 'when drinking':
            smokes_nums.append(2)
        if data.iloc[i]['smokes'] == 'sometimes':
            smokes_nums.append(3)
        if data.iloc[i]['smokes'] == 'yes':
            smokes_nums.append(4)
        if data.iloc[i]['smokes'] == 'trying to quit':
            smokes_nums.append(5)
            
        # body type
        if data.iloc[i]['body_type'] == 'thin':
            body_nums.append(1)
        elif data.iloc[i]['body_type'] == 'skinny':
            body_nums.append(2)
        elif data.iloc[i]['body_type'] == 'fit':
            body_nums.append(3)
        elif data.iloc[i]['body_type'] == 'athletic':
            body_nums.append(4)
        elif data.iloc[i]['body_type'] == 'jacked':
            body_nums.append(5)
        elif data.iloc[i]['body_type'] == 'curvy':
            body_nums.append(6)
        elif data.iloc[i]['body_type'] == 'full figured':
            body_nums.append(7)
        elif data.iloc[i]['body_type'] == 'a little extra':
            body_nums.append(8)
        elif data.iloc[i]['body_type'] == 'overweight':
            body_nums.append(9)
        else:
            body_nums.append(0)    
        
            
    # adding quantified columns to the dataframe       
    data['orient_quantified'] = orient_nums
    data['status_quantified'] = status_nums
    data['body_quantified'] = body_nums
    data['smokes_quantified'] = smokes_nums
    data['drinks_quantified'] = drinks_nums
    
    
    if 'income' in keepers:
        for i in data.index:
            if data.loc[i]['income'] == -1:
                data = data.drop(i, 0)
    
    # picking the two attributes we'd like to graph against one another
    for column in data:
        if column not in keepers:
            data = data.drop(column, 1)
            
    
    return data
    
       
# enteirng the attributes to be graphed against one another
X = "drinks_quantified"
Y = "smokes_quantified"
keepers = [X, Y]
                              
if __name__ == "__main__":
    # THIS CODE TAKES APPROX 37 SECONDS TO RUN
    # opening the data
    data = open_file('profiles.csv.zip')
    # determining points using schosen attributes
    points = get_points(data, keepers)
    # graphing the information into a heatmap
    graph_clusters(points,keepers)
    
    
    
        

        
    




    

  