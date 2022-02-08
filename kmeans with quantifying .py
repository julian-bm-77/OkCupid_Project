'''
    DS2500
    Spring 2021
    Code from class: k-means clustering
'''

import math
import plotly.io as pio
import plotly.express as px
from plotly.offline import plot
import json
import pandas as pd
import numpy as np
from random import sample
import seaborn as sns
# from get_movies import query_movies




def distance(p1, p2):
    """ Function: distance
        Parameters: two points, lists of equal length (floats)
        Returns: a float, the euclidian distance between the two points 
    """
    d = 0
    for i in range(len(p1)):
        d += (p1[i] - p2[i]) ** 2
    return math.sqrt(d) 
    

def closest(point, centroids):
    ''' Function: closest 
        Parameters: one point (list of floats), and a list of
                    centroids (2d list of floats)
        Returns: position of the closest centroid
    '''
    closest = 0
    curr_min = distance(point, centroids[0])
    for i in range(1, len(centroids)):
        d = distance(point, centroids[i])
        if d < curr_min:
            curr_min = d
            closest = i
    return closest

def assign_clusters(centroids, points):
    ''' Function: assign_clusters
        Parameters: 2d list of centroids (floats), dataframe with points
        Returns: updated dataframe with centroid column
    '''
    close = []
    
    # Iterate over dataframe by index
    for ind in points.index:
        point = (points[X][ind], points[Y][ind])
        centroid = closest(point, centroids)
        close.append(centroid)
    
    # Now I have a list of centroid #s, which is the same length
    # as the number of points
    points["centroid"] = close
    return points
        

def graph_clusters(clusters, keepers):
    """ Function: graph_clusters
        Parameters: dtaframe of clusters, where centroids is a column
        Returns: nothing, just renders the plot
    """
    name = 'graphing ' + keepers[0] + ' against ' + keepers[1]
    pio.renderers.default = 'browser'
    fig = px.scatter(clusters, x = clusters[X], y = clusters[Y], color = clusters["centroid"],
                     title= name)
    
    fig.update_traces(marker = dict(size = 12))
    plot(fig)




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
    
    
    
    # picking the two attributes we'd like to graph against one another
    for column in data:
        if column not in keepers:
            data = data.drop(column, 1)
            
    
    return data
    
def k_means(data, keepers):
    points = get_points(data, keepers)
    print(points)
    
      
    # Pick the first set of centroids
    centroids = points.sample(n = K)
    centroids = centroids.values.tolist()
    print(centroids)
    new_centroids = []
       
    for i in range(10):
        # Assign every point to its closest centroid
        df = assign_clusters(centroids, points)
        graph_clusters(df, keepers)
        
        # Compute centroids for real
        centroids = []
        for j in range(K):
            cluster = df[df["centroid"] == j]
            mean_x = cluster[X].mean()
            mean_y = cluster[Y].mean()
            centroids.append([mean_x, mean_y])
            
# assigning our K value and picking the attributes we'd like to graph
K = 9
X = "age"
Y = "smokes_quantified"
to_graph = [X, Y]
                              
if __name__ == "__main__":

    data = open_file('profiles.csv.zip')
    # creating and visualizing k-means clusters
    k_means(data, to_graph)
    
    
        

        
    




    

  