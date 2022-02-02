# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:40:05 2022

@author: Emma
"""
import pandas as pd
import numpy as np


class WrongColumnsName(Exception):
    """Exception raised in read_and_chek function when dataframe columns are wrong"""

def read_and_check(filename, sheet):
    """
    This function read the data file and check if it is has a proper format.

    Parameters
    ----------
    filename : str
        Path of a dataframe file with .xlsx extension.
    sheet : str
        Sheet name, it must be among 'temi', 'caratteristiche' and 'punteggio'.

    Returns
    -------
    DataFrame

    """  
    possible_sheets = ['temi', 'caratteristiche','punteggio']
    topic_possible_columns = ['Gruppo','Tema','Intenzione', 'Risultato', 'Percezione']
    elements_possible_columns = ['Gruppo', 'Elemento caratteristico', 'Utilizzo', 'Coerenza']
    score_possible_columns = ['Gruppo', 'Punteggio tecnico', 'Punteggio pubblico']
    
    if ".xlsx" not in filename: 
        raise ValueError("Sorry, data files must have .xlsx extension.")     
    if sheet not in possible_sheets:
        raise ValueError("Sorry, sheet name must be among 'temi', 'caratteristiche' and 'punteggio'. It is case sensitive.")
    else:
        original_df = pd.read_excel(filename, sheet_name=sheet) 
        if (sheet == "temi") and \
            (all([c in original_df.columns for c in topic_possible_columns])): 
                df = original_df.copy()
                df.name = "topics"
                return df
        elif (sheet == "caratteristiche") and \
              (all([c in original_df.columns for c in elements_possible_columns])): 
                df = original_df.copy()
                df.name = "elements"
                return df  
        elif (sheet == "punteggio") and \
              (all([c in original_df.columns for c in score_possible_columns])): 
                df = original_df.copy()
                df.name = "score"
                return df 
        else:
              raise WrongColumnsName("Sorry, columns names are not as expected.") 
    

def extract_groups_names(df):
    """"This funcion get a dataframe, check the column named "group" and
    iterate through its elements to return a list with all the different 
    names of groups.
    
    Parameters
    ----------
    df : dataframe

    Returns
    -------
    list
    
    """
    groups = []
    G = np.asarray(df.loc[:,"Gruppo"])
    for i in range (0,len(G)):
       if (G[i-1]!= G[i]):
           groups.append(G[i])
    return(groups)

def calculate_group_score(df_elements, df_score, group):   
    df_elements_filtered = df_elements.query("Gruppo == @group")
    
    el_use = df_elements_filtered.loc[:,"Utilizzo"]
    el_coh = df_elements_filtered.loc[:,"Coerenza"] 
    p_score = df_score.loc[group, "Punteggio pubblico"]
    j_score = df_score.loc[group, "Punteggio tecnico"]
    
    u = np.asarray(el_use)
    c = np.asarray(el_coh)
    elements_score = np.sum(u*c)
    group_score = (2*elements_score + 2*j_score + p_score)/5
    group_score = round (group_score, 2)
    return(group_score)

def count_and_join(df, score):
    df_condition_count = df.groupby(['Gruppo']).count().drop(['Intenzione','Risultato','Percezione'], axis=1)
    df_condition_count.rename(columns={'Tema':'Count'}, inplace = True)
      
    df_topic_count = df[['Gruppo', 'Tema']].groupby(['Gruppo']).aggregate({'Tema':'/'.join})
      
    df_join = pd.concat([df_condition_count, df_topic_count, score], axis=1, join='outer')
    df_join.fillna(0, inplace=True)
    df_join.rename(columns={'index':'Group', 'Tema': 'Topic type'}, inplace=True) 
    return(df_join)

def calculate_correlation(x,y):
    x = np.asarray(x)
    y = np.asarray(y)
    N = len(x)
    num = N*np.sum(x*y) - (np.sum(x) * np.sum(y))
    den = np.sqrt((N*np.sum(x**2) - np.sum(x)**2) * (N * np.sum(y**2) - np.sum(y)**2))
    R = num/den
    return(R)


# def animate_plot():
    
#     return(animated_plot)



