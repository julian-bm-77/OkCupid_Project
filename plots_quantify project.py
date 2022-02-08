'''
    DS2500
    Spring 2021
    Code from class: k-means clustering
'''

import plotly.express as px
import pandas as pd

def open_file(data):
    ''' Function: open_file
        Parameters: filename of csv file
        Returns: a pandas DataFrame
    '''
    
    #CREATING OKCUPID DATAFRAME FROM CSV
    data = pd.read_csv(data)

    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data
data = open_file('profiles.csv.zip')
def quantify_values(file, columns):
    ''' Function: quantify_values
        Parameters: filename of csv file, columns to keep in returned dataframe
        Returns: quantified numerical values in a more specific dataframe given by input
    '''
    # creating lists for each quantified value to later add to df
    orient_nums = []
    status_nums = []
    drinks_nums = []
    smokes_nums = []
    body_nums = []

    #opening file and cleaning
    data = open_file(file)

    # quantifying sexual orientation
    for i in data.index:
        if data.loc[i]['orientation'] == 'straight':
            # appending to list
            orient_nums.append(0)
        elif data.loc[i]['orientation'] == 'bisexual':
            orient_nums.append(3)
        elif data.loc[i]['orientation'] == 'gay':
            orient_nums.append(6)
        else:
            orient_nums.append(float("NaN"))
    # quanitifying dating status
    for i in data.index:
        
        if data.loc[i]['status'] == 'single':
            status_nums.append(1)
        elif data.loc[i]['status'] == 'seeing someone':
            status_nums.append(3)
        elif data.loc[i]['status'] == 'available':
            status_nums.append(2)
        elif data.loc[i]['status'] == 'married':
            status_nums.append(4)
        else:
            status_nums.append(float("NaN"))
    # quantifying drinking habits
    for i in data.index:        
        if data.iloc[i]['drinks'] == 'not at all':
            drinks_nums.append(1)
        elif data.iloc[i]['drinks'] == 'rarely':
            drinks_nums.append(2)
        elif data.iloc[i]['drinks'] == 'socially':
            drinks_nums.append(3)
        elif data.iloc[i]['drinks'] == 'often':
            drinks_nums.append(4)
        elif data.iloc[i]['drinks'] == 'very often':
            drinks_nums.append(5)
        elif data.iloc[i]['drinks'] == 'desperately':
            drinks_nums.append(6)
        else:
            drinks_nums.append(float("NaN"))
    for i in data.index:
        if data.iloc[i]['smokes'] == 'no':
            smokes_nums.append(1)
        elif data.iloc[i]['smokes'] == 'when drinking':
            smokes_nums.append(2)
        elif data.iloc[i]['smokes'] == 'sometimes':
            smokes_nums.append(3)
        elif data.iloc[i]['smokes'] == 'yes':
            smokes_nums.append(4)
        elif data.iloc[i]['smokes'] == 'trying to quit':
            smokes_nums.append(5)
        else:
            smokes_nums.append(float("NaN"))
            
    for i in data.index:
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
        elif data.iloc[i]['body_type'] == 'average':
            body_nums.append(6)
        elif data.iloc[i]['body_type'] == 'curvy':
            body_nums.append(6)
        elif data.iloc[i]['body_type'] == 'full figured':
            body_nums.append(7)
        elif data.iloc[i]['body_type'] == 'a little extra':
            body_nums.append(8)
        elif data.iloc[i]['body_type'] == 'overweight':
            body_nums.append(9)
        else:
            body_nums.append(float("NaN"))    
    # adding results in lists to new columns and updating dataframe
    data['orient_num'] = orient_nums
    data['status_num'] = status_nums
    data['body_num'] = body_nums
    data['smokes_num'] = smokes_nums
    data['drinks_num'] = drinks_nums
    
    #dropping unimportant columns
    for column in data:
        if column not in columns:
            data = data.drop(column, 1)
    # making negative incomes NaN values
    data['income'] = data['income'].replace([-1],float('NaN'))
    # dropping rows which have NaN values
    data.dropna(inplace = True)
    data.reset_index(drop= False)
    return data
def plot(df, X, Y):
    ''' Function: plot
        Parameters: dataframe, name of column in dataframe on x axis, name of column in dataframe on y axis
        Returns: 
    '''
    fig = px.scatter(df, x= X, y= Y, trendline="ols", title = (str(X) + " vs. " + str(Y)))
    fig.show()
if __name__ == "__main__":
    keepers = ['smokes_num', 'drinks_num', 'body_num', 'status_num', 'orient_num', 'age', 'height', 'income']
    data = quantify_values('profiles.csv.zip', keepers)
    # create age vs income plot
    age_income = plot(data, 'age', 'income')
    # create body type vs smokes
    fig2 = plot(data, 'body_num', 'smokes_num')
    # create body type vs age
    fig3 = plot(data, 'body_num', 'age')   
    # # age vs orientation
    fig4 = plot(data, 'age', 'orient_num') 
    # # height vs income
    fig5 = plot(data, 'height', 'income')
    # status vs income
    fig6 = plot(data, 'status_num', 'income')
    # drinking habits vs smoking habits
    fig7 = plot(data, 'drinks_num', 'smokes_num')
    # drinking habits vs. dating status
    fig8 = plot(data, 'drinks_num', 'status_num')
        
    




    

  