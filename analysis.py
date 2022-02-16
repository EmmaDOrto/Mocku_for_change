"""
Created on Thu Jan 27 10:40:26 2022

@author: Emma
"""
import pandas as pd
from matplotlib import pyplot as plt
import functions as f
import sys
import configparser
import os

file_name = sys.argv[1]
config = configparser.ConfigParser()
config.read(sys.argv[2])

results_path = config.get('paths','analysis_results')

dest1 = config.get('paths','plot1')
dest2 = config.get('paths','plot2')
dest3 = config.get('paths','plot3')
dest4 = config.get('paths','plot4')
dest5 = config.get('paths','plot5')
dest6 = config.get('paths','plot6')
dest7 = config.get('paths','plot7')
dest8 = config.get('paths','plot8')

plot_destinations = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8]

df = f.read_and_check("thesis_data.xlsx", "topics")
df_elements = f.read_and_check("thesis_data.xlsx", "elements")
df_score = f.read_and_check("thesis_data.xlsx", "score")


conditions = {"Topic present in intention": "Intention =='Present'", 
              "Topic present or slightly present in intention": "Intention =='Present'| Intention =='Slightly'",
              "Topic present in result": "Result =='Present'",      
              "Topic present or slightly present in result": "Result =='Present'| Result =='Slightly'",      
              "Topic present in perception": "Perception =='Present'",
              "Topic present or slightly present in perception": "Perception =='Present'| Perception =='Slightly'",
              "Topic present in intention or result or perception": "Intention =='Present'| Result =='Present' | Perception =='Present'",
              "Topic present or slighlty present in intention or result or perception": "Intention =='Present'| Intention =='Slightly'| Result =='Present' | Result =='Slightly' | Perception =='Present' | Perception =='Slightly'"
           
              }

groups = f.extract_group_names(df)

genre_scores = []
for group in groups:
    group_score = f.calculate_group_score(df_elements, df_score, group)
    genre_scores.append(group_score)
score = pd.Series(genre_scores, index = groups, name = "Score")

correlations = []
correlations_squared = []
for key,destination in zip(conditions,plot_destinations):
    
    df_filtered = df.query(conditions[key]) 
    
    df_counted = f.count_fulfillments(df_filtered)
    
    df_final = pd.concat([df_counted, score], axis=1, join='outer')
   
    
    df_final_name = (key)
    
    if not os.path.exists(results_path):
        df_final.to_excel(results_path, sheet_name = df_final_name, index=True)

    else:
        with pd.ExcelWriter(results_path, engine='openpyxl', if_sheet_exists='replace', mode='a') as writer:
            df_final.to_excel(writer, sheet_name=df_final_name, index=True)

    x = df_final.Score
    y = df_final.Count
    plt.scatter(x,y, s=100, c='blue')
    plt.title(df_final_name)
    plt.xlabel('Genre score',fontsize=12)
    plt.ylabel('Topics count',fontsize=12)
    for i in range(df_final.shape[0]): 
        plt.text(x=x[i]+0.1,y=y[i]+0.1,s=df_final.index[i])
    plt.savefig(destination)
    plt.close()
    
    R = f.calculate_correlation(x,y)
    correlations.append(round(R,2))
    correlations_squared.append(round(R**2, 2))

conditions_names = list(conditions.keys()) 
condition_score_correlations = pd.DataFrame(list(zip(correlations, correlations_squared)), index = conditions_names,
               columns =['Pearson coefficient', 'R^2']).sort_values("R^2", ascending=False)
                                            
with pd.ExcelWriter(results_path, engine='openpyxl', if_sheet_exists='replace', mode='a') as writer:
    condition_score_correlations.to_excel(writer, sheet_name= "condition-score correlations", index=True)