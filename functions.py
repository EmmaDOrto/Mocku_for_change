# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 12:40:05 2022

@author: Emma
"""
import pandas as pd

def import_and_clean(filename, sheet):
    original_df = pd.read_excel(filename + ".xlsx", sheet_name=sheet)
    df = original_df.copy()
    df.fillna('Assente', inplace=True)
    return(df)


def filter_and_count(df, condition):
       
    return(df_join)


def calculate_genre_score():
    
    return(score)

def calculate_correlation():
    
    return(correlation)

def graph_plot():
    
    return(plot)


def animate_plot():
    
    return(animated_plot)



