# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:49:25 2022

@author: Emma
"""
import functions as f
import pandas as pd
import pandas.testing as pt
import pytest

# read_and_check ----------------------------------------------

def test_return_a_df_same_as_original_1():
    
    expected = pd.read_excel("thesis_data.xlsx", "topics")
    result = f.read_and_check("thesis_data.xlsx", "topics")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_2():
    
    expected = pd.read_excel("thesis_data.xlsx", "elements")
    result = f.read_and_check("thesis_data.xlsx", "elements")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_3():
    
    expected = pd.read_excel("thesis_data.xlsx", "score")
    result = f.read_and_check("thesis_data.xlsx", "score")
    
    pt.assert_frame_equal(expected, result)
    
def test_raises_for_csv_file():
    
    filename = "testing_files/thesis_data.csv"
    
    with pytest.raises(ValueError):
        f.read_and_check(filename, "topics")    
        
def test_raises_for_wrong_sheet():
    
    sheet = "tema"
    
    with pytest.raises(ValueError):
        f.read_and_check("thesis_data.xlsx", sheet)
        
def test_raises_for_wrong_column_names():
    
    filename = "testing_files/thesis_data_wrong_column.xlsx"
    
    with pytest.raises(f.WrongColumnNames):
        f.read_and_check(filename, "topics")
        

    
