"""
Created on Thu Jan 27 10:40:26 2022

@author: Emma
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import functions as f

df = f.import_and_copy("thesis_data", "temi")


conditions = {"1": { "description": "Topic present in intention", "code": "Intenzione =='Presente'"}, 
              "2": { "description": "Topic present or slightly present in intention", "code": "Intenzione =='Presente'| Intenzione =='Debole'"},
              "3": { "description": "Topic present in result", "code": "Risultato =='Presente'"},      
              "4": { "description": "Topic present or slightly present in result", "code": "Risultato =='Presente'| Risultato =='Debole'"},      
              "5": { "description": "Topic present in perception", "code": "Percezione =='Presente'"},
              "6": { "description": "Topic present or slightly present in perception", "code": "Percezione =='Presente'| Percezione =='Debole'"},
             }

groups = []
G = np.asarray(df.loc[:,"Gruppo"])

for k in range (0,len(G)):
   if (G[k-1]!= G[k]):
      groups.append(G[k])

df_elements = f.import_and_copy("Thesis_data", "caratteristiche")
df_score = f.import_and_copy("Thesis_data", "punteggio")
df_score = df_score.set_index("Gruppo")


genre_score = []

for group in groups:
    
    df_elements_filtered = df_elements.query("Gruppo == @group")
    element_use = df_elements_filtered.loc[:,"Utilizzo"]
    element_coherence = df_elements_filtered.loc[:,"Coerenza"]
    pub_score = df_score.loc[group, "Punteggio pubblico"]
    jury_score = df_score.loc[group, "Punteggio tecnico"]
    
    
    group_score = f.calculate_group_score(element_use, element_coherence, pub_score, jury_score)
    genre_score.append(group_score)
    

score = pd.Series(genre_score, index = groups, name = "Punteggio")


for key in conditions:
    
    df_filtered = df.query(conditions[key]["code"])
    df_count = df_filtered.groupby(['Gruppo']).count().drop(['Intenzione','Risultato','Percezione'], 
                                                            axis=1).rename(columns={'Tema':'N_temi'})
    df_cond = df_filtered[['Gruppo', 'Tema']].groupby(['Gruppo']).aggregate({'Tema':'/'.join})
    df_join = pd.concat([df_cond, df_count, score], axis=1, join='inner')
    df_join.rename(columns={'index':'Gruppo', 'Tema': 'Tipo'}, inplace=True) 
    
    print(conditions[key]["description"])
    print(df_join) 


    x = df_join.loc[:,"Punteggio"]
    y = df_join.loc[:,"N_temi"]
    plt.scatter(x,y, s=100, c='blue')
    plt.xlabel('Punteggio di genere',fontsize=12)
    plt.ylabel('Conteggio temi',fontsize=12)
    plt.show()
   
    R = f.calculate_correlation(x,y)
    print("Correlazione = ",R)