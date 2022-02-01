# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:40:05 2022

@author: Emma
"""
import pandas as pd
import numpy as np

def import_and_copy(filename, sheet):
    original_df = pd.read_excel(filename + ".xlsx", sheet_name=sheet)
    df = original_df.copy()
    return(df)

def extract_groups_names(df):
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



