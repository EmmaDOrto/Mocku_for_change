# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:40:05 2022

@author: Emma
"""
import pandas as pd
import numpy as np


class WrongColumnNames(Exception):
    """Exception raised in read_and_chek function when dataframe columns are wrong"""

def read_and_check(filename, sheet):
    """
    This function read the data file and check if it is has a proper format.

    Parameters
    ----------
    filename : str
        Path of a dataframe file with .xlsx extension.
    
    sheet : str
        Sheet name, it must be among 'topics', 'elements' and 'score'.

    Returns
    -------
    df : DataFrame

    """  
    possible_sheets = ['topics', 'elements','score']
    topic_possible_columns = ['Group','Topic','Intention', 'Result', 'Perception']
    elements_possible_columns = ['Group', 'Typical element', 'Use', 'Coherence']
    score_possible_columns = ['Group', 'Jury score', 'Audience score']
    
    if ".xlsx" not in filename: 
        raise ValueError("Sorry, data files must have .xlsx extension.")     
    if sheet not in possible_sheets:
        raise ValueError("Sorry, sheet name must be among 'topics', 'elements' and 'score'. It is case sensitive.")
    else:
        original_df = pd.read_excel(filename, sheet_name=sheet) 
        if (sheet == "topics") and \
            (all([c in original_df.columns for c in topic_possible_columns])): 
                df = original_df.copy()
                df.name = "topics"
                return df
        elif (sheet == "elements") and \
              (all([c in original_df.columns for c in elements_possible_columns])): 
                df = original_df.copy()
                df.name = "elements"
                return df  
        elif (sheet == "score") and \
              (all([c in original_df.columns for c in score_possible_columns])): 
                df = original_df.copy()
                df.name = "score"
                df.set_index("Group", inplace= True)
                df.index.name = "Group"
                return df 
        else:
              raise WrongColumnNames("Sorry, columns names are not as expected.") 
    

def extract_group_names(df):
    """"This funcion get a dataframe, check the column named "group" and
    iterate through its elements to return a list with all the different 
    names of groups.
    
    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    group_names : list
    
    """
    
    G = np.asarray(df.loc[:,"Group"])
    group_names = {x.capitalize() for x in G} 
    group_names = sorted(group_names)
    return(group_names)
    

def calculate_group_score(df_elements, df_score, group): 
    
    """
    This function get the two dataframe with the needed info
    and the name of the group and calculate the group score value.
    
    
    Parameters
    ----------
    df_elements : DataFrame
        It must contains following columns: Group, Use, Coherence.
    
    df_score : DataFrame
        It must contains following columns: Group, Audience score, Jury score.
    
    group : str
       Must be among 'Group' column elements from both df_elements and df_score.

    Returns
    -------
    group_score : numpy.float64
            Value between 0 and 5.
    
    """
    df_elements_filtered = df_elements[df_elements.Group == group]

    el_use = df_elements_filtered.loc[:,"Use"]
    el_coh = df_elements_filtered.loc[:,"Coherence"] 
    p_score = df_score.loc[group, "Audience score"]
    j_score = df_score.loc[group, "Jury score"]
    
    u = np.asarray(el_use)
    c = np.asarray(el_coh)
    elements_score = np.sum(u*c)
    group_score = (3*j_score + elements_score + p_score)/5
    group_score = round (group_score, 2)
    return(group_score)

def count_fulfillments(df):
    """
    This function gets a filtered by condition dataframe and counts 
    how many topics (and of which type) fulfill that condition. 
    
    Parameters
    ----------
    df : DataFrame
        
    Returns
    -------
    df_join : Dataframe
    
    """
    df_count = df.groupby(['Group']).count()
    df_count = df_count.drop(['Intention','Result','Perception'], axis=1)
    df_count.rename(columns={'Topic':"Count"}, inplace = True)
      
    df_topic_type = df[['Group', 'Topic']].groupby(['Group']).aggregate({'Topic':'/'.join})
      
    df_join = pd.concat([df_count, df_topic_type], axis=1, join='inner')
    df_join.rename(columns={'index':'Group', 'Topic': 'Topic type'}, inplace=True) 
    
    return(df_join)

def calculate_correlation(x,y):
    """
    This function calculate the pearson coefficent of correlation between sets x and y.

    Parameters
    ----------
    x : numpy.array
        Its lenght must be same as y.
        
    y : numpy.array
        Its lenght must be same as x.
    
    Returns
    -------
    R : numpy.float64
        Value between -1 and 1.

    """
    x = np.asarray(x)
    y = np.asarray(y)
    N = len(x)
    num = N*np.sum(x*y) - (np.sum(x) * np.sum(y))
    den = np.sqrt((N*np.sum(x**2) - np.sum(x)**2) * (N * np.sum(y**2) - np.sum(y)**2))
    R = num/den
    return(R)




