"""
Created on Thu Jan 27 10:40:26 2022

@author: Emma
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import functions as f

df = f.import_and_copy("thesis_data", "temi")
#df = df.fillna('Assente', inplace=True)


conditions = {"1": { "description": "Topic present in intention", "code": "Intenzione =='Presente'"}, 
              "2": { "description": "Topic present or slightly present in intention", "code": "Intenzione =='Presente'| Intenzione =='Debole'"},
              "3": { "description": "Topic present in result", "code": "Risultato =='Presente'"},      
              "4": { "description": "Topic present or slightly present in result", "code": "Risultato =='Presente'| Risultato =='Debole'"},      
              "5": { "description": "Topic present in perception", "code": "Percezione =='Presente'"},
              "6": { "description": "Topic present or slightly present in perception", "code": "Percezione =='Presente'| Percezione =='Debole'"},
             }

index_name = ['G' + str(i) for i in range(1,8)]
score = pd.Series([1.97, 1.54, 2.93, 4.60, 4.61, 3.46, 4.53], 
                  index = index_name, name = 'Punteggio')


for key in conditions:
    
    df_filtered = df.query(conditions[key]["code"])
    df_count = df_filtered.groupby(['Gruppo']).count().drop(['Intenzione','Risultato','Percezione'], 
                                                            axis=1).rename(columns={'Tema':'N_temi'})
    df_cond = df_filtered[['Gruppo', 'Tema']].groupby(['Gruppo']).aggregate({'Tema':'/'.join})
    df_join = pd.concat([df_cond, df_count, score], axis=1, join='inner').reset_index().sort_values('Punteggio')
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
   

    
    