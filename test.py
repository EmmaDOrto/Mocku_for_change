# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:49:25 2022

@author: Emma
"""
import functions as f
import pandas as pd
import numpy as np
import pandas.testing as pt
import pytest

# read_and_check ----------------------------------------------

def test_return_a_df_same_as_original_1():
    
    expected = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    result = f.read_and_check("testing_files/thesis_data_test.xlsx", "topics")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_2():
    
    expected = pd.read_excel("testing_files/thesis_data_test.xlsx", "elements")
    result = f.read_and_check("testing_files/thesis_data_test.xlsx", "elements")
    
    pt.assert_frame_equal(expected, result)
    
def test_raises_for_csv_file():
    
    filename = "testing_files/thesis_data.csv"
    
    with pytest.raises(ValueError):
        f.read_and_check(filename, "topics")    
        
def test_raises_for_wrong_sheet():
    
    sheet = "tema"
    
    with pytest.raises(ValueError):
        f.read_and_check("testing_files/thesis_data_test.xlsx", sheet)
        
def test_raises_for_wrong_column_names():
    
    filename = "testing_files/thesis_data_wrong_column.xlsx"
    
    with pytest.raises(f.WrongColumnNames):
        f.read_and_check(filename, "topics")
        
def test_change_df_index():
    
    df = f.read_and_check("testing_files/thesis_data_test.xlsx", "score")
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    result = list(df.index.values)
    
    assert  expected == result  
     
def test_change_df_index_name():
    
    df_score = f.read_and_check("testing_files/thesis_data_test.xlsx", "score")
    
    assert df_score.index.name == "Group"
 

# extract_group_names -----------------------------------------

def test_return_expected_list():
    
    df = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    result = f.extract_group_names(df)
    
    assert expected == result

def test_return_expected_list_from_unsorted_df_column():
    
    unsorted_df = pd.DataFrame({
        "Group" : ["G7", "G1", "G5", "G2", "G2", "G3", "G1", 
                   "G4", "G3", "G5", "G4", "G6", "G7", "G1"],
        "Irrelevant" :["i", "i", "i", "i", "i", "i", "i",
                       "i", "i", "i", "i", "i", "i", "i"]
        })
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    
    result = f.extract_group_names(unsorted_df)
    
    assert expected == result
    
def test_mixed_case_Gn():  
    
    mixed_case_df = pd.DataFrame({
        "Group" : ["G7", "g1", "G5", "g2", "g2", "G3", "g1", 
                   "G4", "G3", "G5", "g4", "G6", "g7", "G1"],
        "Irrelevant" :["i", "i", "i", "i", "i", "i", "i",
                       "i", "i", "i", "i", "i", "i", "i"]
        })
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    
    result = f.extract_group_names(mixed_case_df)
    
    assert expected == result
    
def test_mixed_case():  
    
    mixed_case_df = pd.DataFrame({
        "Group" : ["Mario", "g1", "G5", "g2", "maRio", "G3", "g6", 
                   "G4", "MARIO", "G5", "g4", "mario", "g7", "G1"],
        "Irrelevant" :["i", "i", "i", "i", "i", "i", "i",
                       "i", "i", "i", "i", "i", "i", "i"]
        })
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7","Mario"]
    
    result = f.extract_group_names(mixed_case_df)
    
    assert expected == result
 
    
# calculate_group_score ---------------------------------------

def test_return_expected_value():
    
    df1 = pd.read_excel("thesis_data.xlsx", "elements")
    df2 = pd.read_excel("thesis_data.xlsx", "score")
    df2.set_index("Group", inplace= True)
    df2.index.name = "Group"
    
    expected_score = 1.76
    
    result = f.calculate_group_score(df1, df2, 'G1')
    
    assert  expected_score == result 

def test_return_value_between_0_and_5(): 
    
    df1 = pd.read_excel("testing_files/thesis_data_test.xlsx", "elements")
    df2 = pd.read_excel("testing_files/thesis_data_test.xlsx", "score")
    df2.set_index("Group", inplace= True)
    df2.index.name = "Group"
    group = 'G2'
    
    result = f.calculate_group_score(df1, df2, group)
    
    assert  0 <= result <= 5
    
# count_fulfillments ----------------------------------------------

def test_df_shape():
    df = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    
    df2 = f.count_fulfillments(df)
    
    df_shape = list(df2.shape)
    
    expected_df_shape = [7,2]
    
    assert df_shape == expected_df_shape
    

# calculate_correlation --------------------------------------

def test_return_correct_value():
    x = [1,2,3,4,5,6,7,8,9]
    y = [1,2,3,4,5,6,7,8,9]
    
    result = f.calculate_correlation(x,y)
    
    assert  result == 1

def test_result_between_minus1_and_1_random_values():    
    
    x = np.random.rand(10)
    y = np.random.rand(10)
    
    result = f.calculate_correlation(x,y)
    
    assert  -1 <= result <= 1
    
  
    