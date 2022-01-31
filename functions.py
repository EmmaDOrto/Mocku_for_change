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

def calculate_group_score(element_use, element_coherence, pub_score, jury_score):   
    u = np.asarray(element_use)
    c = np.asarray(element_coherence)
    elements_score = np.sum(u*c)
    group_score = (2*elements_score + 2*jury_score + pub_score)/5
    group_score = round (group_score, 2)
    return(group_score)

# def filter_and_count(df, condition):
       
#     return(df_join)


def calculate_correlation(x,y):
    N = len(x)
    x = np.asarray(x)
    y = np.asarray(y)
    num = N*np.sum(x*y) - (np.sum(x) * np.sum(y))
    den = np.sqrt((N*np.sum(x**2) - np.sum(x)**2) * (N * np.sum(y**2) - np.sum(y)**2))
    R = num/den
    return(R)

# def graph_plot():
    
#     return(plot)


# def animate_plot():
    
#     return(animated_plot)



