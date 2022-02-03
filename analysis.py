"""
Created on Thu Jan 27 10:40:26 2022

@author: Emma
"""
import pandas as pd
from matplotlib import pyplot as plt
import functions as f

df = f.read_and_check("thesis_data.xlsx", "topics")
df_elements = f.read_and_check("thesis_data.xlsx", "elements")
df_score = f.read_and_check("thesis_data.xlsx", "score")
df_score.set_index("Group", inplace= True)


conditions = {"Topic present in intention": "Intention =='Present'", 
              "Topic present or slightly present in intention": "Intention =='Present'| Intention =='Slightly'",
              "Topic present in result": "Result =='Present'",      
              "Topic present or slightly present in result": "Result =='Present'| Result =='Slightly'",      
              "Topic present in perception": "Perception =='Present'",
              "Topic present or slightly present in perception": "Perception =='Present'| Perception =='Slightly'",
              }

groups = f.extract_group_names(df)

genre_scores = []
for group in groups: 
    group_score = f.calculate_group_score(df_elements, df_score, group)
    genre_scores.append(group_score)
    
score = pd.Series(genre_scores, index = groups, name = "Score")

correlations = []
for key in conditions:
    
    df_filtered = df.query(conditions[key]) 
    df_counted = f.count_and_join(df_filtered, score)
    df_counted.name = (key)
    
    print(df_counted.name)
    print(df_counted) 

    x = df_counted.Score
    y = df_counted.Count
    plt.scatter(x,y, s=100, c='blue')
    plt.title(df_counted.name)
    plt.xlabel('Genre score',fontsize=12)
    plt.ylabel('Topics count',fontsize=12)
    for i in range(df_counted.shape[0]): 
        plt.text(x=x[i]+0.1,y=y[i]+0.1,s=df_counted.index[i])
    plt.show()
    
    R = f.calculate_correlation(x,y)
    print("Correlation = ", R)
    correlations.append(R)

conditions_names = list(conditions.keys()) 
condition_score_correlations = pd.Series(correlations, index = conditions_names, name= "Correlation with Genre score")

print(condition_score_correlations)