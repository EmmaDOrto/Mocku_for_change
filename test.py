# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:49:25 2022

@author: Emma
"""
import functions as f
import unittest
import pandas as pd
import pandas.testing as pt
import pytest

class WrongColumnsName(Exception):
    """Exception raised in read_and_chek function when dataframe columns are wrong"""


# read_and_check ----------------------------------------------

def test_return_a_df_same_as_original_1():
    
    expected = pd.read_excel("thesis_data.xlsx", "temi")
    result = f.read_and_check("thesis_data.xlsx", "temi")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_2():
    
    expected = pd.read_excel("thesis_data.xlsx", "caratteristiche")
    result = f.read_and_check("thesis_data.xlsx", "caratteristiche")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_3():
    
    expected = pd.read_excel("thesis_data.xlsx", "punteggio")
    result = f.read_and_check("thesis_data.xlsx", "punteggio")
    
    pt.assert_frame_equal(expected, result)
    
def test_raises_for_csv_file():
    
    filename = "thesis_data.csv"
    
    with pytest.raises(ValueError):
        f.read_and_check(filename, "temi")    
        
def test_raises_for_wrong_sheet():
    
    sheet = "tema"
    
    with pytest.raises(ValueError):
        f.read_and_check("thesis_data.xlsx", sheet)
        
def test_raises_for_wrong_column_names():
    
    filename = "thesis_data_wrong_column.xlsx"
    
    with pytest.raises(WrongColumnsName):
        f.read_and_check(filename, "temi")
        
# extract_groups_names -----------------------------------------


# calculate_group_score ---------------------------------------

