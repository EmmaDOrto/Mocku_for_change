"""
Created on Thu Jan 27 10:40:26 2022

@author: Emma
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import functions as f

df= f.import_and_clean("thesis_data", "temi")

cond_names = ["cond_" + str(i) for i in range(1,5)]
conditions = pd.Series(["Risultato =='Presente'", 
                        "Risultato =='Presente'| Risultato =='Debole'", 
                        "(Risultato =='Presente' | Risultato =='Debole') & (Percezione == 'Presente'| Percezione =='Debole')", 
                        "Intenzione =='Presente' & Risultato =='Presente' & Percezione == 'Presente'"], 
                  index = cond_names, name = 'Condizione')


index_name = ['G' + str(i) for i in range(1,8)]
score = pd.Series([1.97, 1.54, 2.93, 4.60, 4.61, 3.46, 4.53], 
                  index = index_name, name = 'Punteggio')


for cond in conditions:
    df_filtered = df.query(cond)
    df_count = df_filtered.groupby(['Gruppo']).count().drop(['Intenzione','Risultato','Percezione'], 
                                                            axis=1).rename(columns={'Tema':'N_temi'})
    df_cond = df_filtered[['Gruppo', 'Tema']].groupby(['Gruppo']).aggregate({'Tema':'/'.join})
    df_join = pd.concat([df_cond, df_count, score], axis=1, join='inner').reset_index().sort_values('Punteggio')
    df_join.rename(columns={'index':'Gruppo', 'Tema': 'Tipo'}, inplace=True) 
    
    print(df_join) 


    x = df_join.loc[:,"Punteggio"]
    y = df_join.loc[:,"N_temi"]
    plt.scatter(x,y, s=100, c='green')
    plt.show()
   
    
   

    
    