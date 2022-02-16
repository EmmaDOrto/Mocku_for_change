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
    """
    This test check if the function returns a dataframe equal to 
    the original file for "topics" sheet.

    """
    expected = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    result = f.read_and_check("testing_files/thesis_data_test.xlsx", "topics")
    
    pt.assert_frame_equal(expected, result)
    
def test_return_a_df_same_as_original_2():
    """
    This test check if the function returns a dataframe equal to 
    the original file for "elements" sheet.

    """
    expected = pd.read_excel("testing_files/thesis_data_test.xlsx", "elements")
    result = f.read_and_check("testing_files/thesis_data_test.xlsx", "elements")
    
    pt.assert_frame_equal(expected, result)
    
def test_raises_for_csv_file():
    """
    This test check if the function raises an error when a .csv file 
    is given as argument.

    """
    filename = "testing_files/thesis_data.csv"
    
    with pytest.raises(ValueError):
        f.read_and_check(filename, "topics")    
        
def test_raises_for_wrong_sheet():
    """
    This test check if the function raises an error when a wrong sheet name 
    is given as argument.

    """
    sheet = "tema"
    
    with pytest.raises(ValueError):
        f.read_and_check("testing_files/thesis_data_test.xlsx", sheet)
        
def test_raises_for_wrong_column_names():
    """
    This test check if the function raises the WrongColumnNames error 
    when column names are wrong.

    """
    filename = "testing_files/thesis_data_wrong_column.xlsx"
    
    with pytest.raises(f.WrongColumnNames):
        f.read_and_check(filename, "topics")
        
def test_change_df_index():
    """
    This test check if the function changes index column of score sheet.

    """
    df = f.read_and_check("testing_files/thesis_data_test.xlsx", "score")
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    result = list(df.index.values)
    
    assert  expected == result  
     
def test_change_df_index_name():
    """
    This test check if the function changes index column name of score sheet.

    """
    df_score = f.read_and_check("testing_files/thesis_data_test.xlsx", "score")
    
    assert df_score.index.name == "Group"
 

# extract_group_names -----------------------------------------

def test_return_expected_list():
    """
    This test check if the function returns the expected array from original df.

    """
    df = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    
    expected = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
    result = f.extract_group_names(df)
    
    assert expected == result

def test_return_expected_list_from_unsorted_df_column():
    """
    This test check if the function returns the expected array from
    a df that has unsorted Group names.

    """
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
    """
    This test check that the function is not case sensitive for
    Group names in the form of g-letter+number.

    """
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
    """
    This test check that the function is not case sensitive for
    g-letter+number and simple string Group names.

    """
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
    """
    This test check that the function returns the expected value for G1.

    """
    df1 = pd.read_excel("thesis_data.xlsx", "elements")
    df2 = pd.read_excel("thesis_data.xlsx", "score")
    df2.set_index("Group", inplace= True)
    df2.index.name = "Group"
    
    expected_score = 1.76
    
    result = f.calculate_group_score(df1, df2, 'G1')
    
    assert  expected_score == result 

def test_return_value_between_0_and_5(): 
    """
    This test check that the function returns ad value between 0 and 5.

    """
    df1 = pd.read_excel("testing_files/thesis_data_test.xlsx", "elements")
    df2 = pd.read_excel("testing_files/thesis_data_test.xlsx", "score")
    df2.set_index("Group", inplace= True)
    df2.index.name = "Group"
    group = 'G2'
    
    result = f.calculate_group_score(df1, df2, group)
    
    assert  0 <= result <= 5
    
def test_expected_0():
    """
    This test check that the function returns expected value for minumum score.

    """
    df1 = pd.DataFrame({ 
     "Group" : ["G1", "G1", "G1", "G1", "G1", 
                "G2", "G3", "G4", "G5", "G6", "G7"],
     "Typical element" : ["Hand-held camera", "Fourth wall breaking", 
                          "Interviews", "Voiceover", "Found footage", 
                          "i", "i", "i", "i", "i", "i"],
     "Use" :[0,0,0,0,0,1,1,1,1,1,1],
     "Coherence" :[0,0,0,0,0,1,1,1,1,1,1]
     })
    df2 = pd.DataFrame({
    "Audience score" :[0,5,5,5,5,5,5],
    "Jury score" :[0,5,5,5,5,5,5]},
    index = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
       )
    group = "G1"
    
    expected_score = 0
    
    result = f.calculate_group_score(df1, df2, group)
    
    assert  expected_score == result    
                
    
def test_expected_5():
    """
    This test check that the function returns expected value for maximum score.

    """
    df1 = pd.DataFrame({ 
     "Group" : ["G1", "G1", "G1", "G1", "G1", 
                "G2", "G3", "G4", "G5", "G6", "G7"],
     "Typical element" : ["Hand-held camera", "Fourth wall breaking", 
                          "Interviews", "Voiceover", "Found footage", 
                          "i", "i", "i", "i", "i", "i"],
     "Use" :[1,1,1,1,1,0,0,0,0,0,0],
     "Coherence" :[1,1,1,1,1,0,0,0,0,0,0]
     })
    df2 = pd.DataFrame({
    "Audience score" :[5,0,0,0,0,0,0],
    "Jury score" :[5,0,0,0,0,0,0]},
    index = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]
       )  
    
    group = "G1"
    
    expected_score = 5
    
    result = f.calculate_group_score(df1, df2, group)
    
    assert  expected_score == result 
        
# count_fulfillments ----------------------------------------------

def test_df_shape():
    """
    This test check that the function returns a df of expected shape.

    """
    df = pd.read_excel("testing_files/thesis_data_test.xlsx", "topics")
    
    df2 = f.count_fulfillments(df)
    
    df_shape = list(df2.shape)
    
    expected_df_shape = [7,2]
    
    assert df_shape == expected_df_shape
    
def test_return_expected_dataframe():
    """
    This test check that the function returns the expected resultant df for 
    a simple given one.

    """
    df = pd.DataFrame({ 
     "Group" : ["G1", "G1", "G2", "G2", "G2", "G3", "G4", "G4",  
                "G5", "G5", "G5", "G6", "G6", "G7", "G7", "G7"],
     "Topic" :["Reality", "Values", "Solutions", "Choices", "Data", 
               "Eco-anxiety", "Agency", "Reality", "Complexity", "Data",
               "Future", "Complexity", "Reality", "Eco-anxiety", "Future", 
               "Data"],
     "Intention" :["irrelevant", "i", "i", "i", "i", "i", "i", "i",
                    "i", "i", "i", "i", "i", "i", "i","i"],
     "Result" :["irrelevant", "i", "i", "i", "i", "i", "i", "i",
                    "i", "i", "i", "i", "i", "i", "i", "i"],
     "Perception" :["irrelevant", "i", "i", "i", "i", "i", "i", "i",
                    "i", "i", "i", "i", "i", "i", "i", "i"]
     })
    
    expected = pd.DataFrame({ 
     "Count" : [2, 3, 1, 2, 3, 2, 3],
     "Topic type" :["Reality/Values", "Solutions/Choices/Data", "Eco-anxiety", 
                    "Agency/Reality", "Complexity/Data/Future", 
                    "Complexity/Reality", "Eco-anxiety/Future/Data"]},
        index = ["G1", "G2", "G3", "G4", "G5", "G6", "G7"], 
     )
    expected.index.name = "Group"
    
    result = f.count_fulfillments(df)
    
    pt.assert_frame_equal(expected, result)
   
# calculate_correlation --------------------------------------

def test_return_value_1():
    """
    This test check that the function returns 1 for maximum positive correlation.

    """
    x = [1,2,3,4,5,6,7,8,9]
    y = [1,2,3,4,5,6,7,8,9]
    
    result = f.calculate_correlation(x,y)
    
    assert  result == 1

def test_return_value_minus1():
    """
    This test check that the function returns -1 for maximum negative correlation.

    """
    x = [1,2,3,4,5,6,7,8,9]
    y = [9,8,7,6,5,4,3,2,1]
    
    result = f.calculate_correlation(x,y)
    
    assert  result == -1

def test_result_between_minus1_and_1():    
    """
    This test check that the function returns a value between -1 and 1.

    """
    x = [5,7,3,2,5,9,0,7,1]
    y = [3,9,7,1,2,4,3,8,6]
    
    result = f.calculate_correlation(x,y)
    
    assert  -1 <= result <= 1
    
  
    