

from __future__ import absolute_import
from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

import os
import sys

import matplotlib.colors as colors

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import sumolib  # noqa
from sumolib.visualization import helpers

import csv
import os


def SetClasse(value):
    if isinstance(value, float):
        if (value >= 0 and value <= 0.15): return 'Free-flow'
        elif (value > 0.15 and value <= 0.33): return 'Reasonably Free-flow'
        elif (value > 0.33 and value <= 0.50): return 'Stable-flow'
        elif (value > 0.50 and value <= 0.60): return 'Approaching unstable-flow'
        elif (value > 0.60 and value <= 0.70): return 'Unstable-flow'
        elif (value > 0.70 and value <= 1.00): return 'Breakdown-flow'
        else:
             return 1 #'Free-flow'
    else:
        return str(value)


def Query(EXP, ROAD, SLOT):
    
    # BASELINE GERAL ***************************************
    df1 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
    df1['Slot'] = df1['Slot'].astype(int)
    df1['Media']  =  df1['Media'].astype(float)
    df1['Velo']  =  df1['Velo'].astype(float)
    df1['Classe']  =  df1['Classe'].astype(float)
    df1['STime']  =  df1['STime'].astype(float)
    df1['Timer']  =  df1['Timer'].astype(float)
    df1['Source'] = "Baseline"

    # df5['ClusterLOS'] =  df5['ClusterLOS'].astype(float)
    df1['ClasseNum'] = df1['Classe'].map(lambda x: SetClasse(x))
    res = df1
    res.sort_values(by=['STime'])
    df1_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]

    # BASELINE 1TO2 ***************************************
    df2 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
    df2['Slot'] = df2['Slot'].astype(int)
    df2['Media']  =  df2['Media'].astype(float)
    df2['Velo']  =  df2['Velo'].astype(float)
    df2['Classe']  =  df2['Classe'].astype(float)
    df2['STime']  =  df2['STime'].astype(float)
    df2['Timer']  =  df2['Timer'].astype(float)
    df2['Source'] = "1TO2"

    df2['ClasseNum'] = df2['Classe'].map(lambda x: SetClasse(x))
    res = df2
    res.sort_values(by=['STime'])
    df2_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]

    # BASELINE RANDOM ***************************************
    df3 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
    df3['Slot'] = df3['Slot'].astype(int)
    df3['Media']  =  df3['Media'].astype(float)
    df3['Velo']  =  df3['Velo'].astype(float)
    df3['Classe']  =  df3['Classe'].astype(float)
    df3['STime']  =  df3['STime'].astype(float)
    df3['Timer']  =  df3['Timer'].astype(float)
    df3['Source'] = "RAND"

    df3['ClasseNum'] = df3['Classe'].map(lambda x: SetClasse(x))
    res = df3
    res.sort_values(by=['STime'])
    df3_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]

    # BASELINE THRESHOLD ***************************************
    df4 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
    df4['Slot'] = df4['Slot'].astype(int)
    df4['Media']  =  df4['Media'].astype(float)
    df4['Velo']  =  df4['Velo'].astype(float)
    df4['Classe']  =  df4['Classe'].astype(float)
    df4['STime']  =  df4['STime'].astype(float)
    df4['Timer']  =  df4['Timer'].astype(float)
    df4['Source'] = "LIM-5"

    df4['ClasseNum'] = df4['Classe'].map(lambda x: SetClasse(x))
    res = df4
    res.sort_values(by=['STime'])
    df4_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]

    # DBSCAN ***************************************
    df5 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
    df5['Slot'] = df5['Slot'].astype(int)
    df5['Media']  =  df5['Media'].astype(float)
    df5['Classe']  =  df5['Classe'].astype(float)
    df5['STime']  =  df5['STime'].astype(float)
    df5['Timer']  =  df5['Timer'].astype(float)
    df5['Clusteres'] =  df5['Clusteres'].astype(int)
    df5['Source'] = "DBSCAN"

    # df5['ClusterLOS'] =  df5['ClusterLOS'].astype(float)
    df5['ClasseNum'] = df5['Classe'].map(lambda x: SetClasse(x))
    res = df5
    res.sort_values(by=['STime'])
    df5_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]
    # *****************************************************************************************

    # XMEANS ***************************************
    df6 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
    df6['Slot'] = df6['Slot'].astype(int)
    df6['Media']  =  df6['Media'].astype(float)
    df6['Media']  =  df6['Media'].astype(float)
    df6['LOS']  =  df6['Classe'].astype(float)
    df6['STime']  =  df6['STime'].astype(float)
    df6['Clusteres'] =  df6['Clusteres'].astype(int)
    df6['Source'] = "X-Means"

    df6['ClasseNum'] = df6['Classe'].map(lambda x: SetClasse(x))
    res = df6
    res.sort_values(by=['STime'])
    df6_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao', 'Classe']]
    # *****************************************************************************************

    res = pd.concat([df1_select,df2_select,df3_select,df4_select,df5_select,df6_select], sort=False)

    res = res[['RoadTag','Slot','Source','Classe','Descricao']]

    # 22|6 - 23|7 - 87|8  (1 sequencia)

    res = res[(res["RoadTag"] == ROAD) & (res["Slot"] == SLOT)]

    los = res.groupby(['Source', 'RoadTag', 'Slot']).mean()

    los['Descricao'] = los['Classe'].map(lambda x: SetClasse(x))
    los['Vehicle'] = EXP

    return los



EXP = "30"
ROAD=87
SLOT=6

wtrResult = csv.writer(open ("result_los_auto.csv", 'a'), delimiter=',', lineterminator='\n')

# wtrResult.writerow (['Source','RoadTag', 'Slot', 'Classe', 'Descricao', 'Vehicle'])

pistas = [[22,6], [23,7], [87,8], [22,4], [23,3], [23,4], [23,5], [87,4], [87,6]]
result = []
for R, S in pistas:
    for C in [30,50,70]: 
        print(str(C) + " - " + str(R) + " - " + str(S))
        los = Query(str(C),R,S)
        los = los.reset_index()
        
        for index, row in los.iterrows():
            wtrResult.writerow ([row["Source"],row["RoadTag"],row["Slot"],row["Classe"],row["Descricao"],row["Vehicle"] ])


# print(result)
# DF = pd.DataFrame(np.asarray(result), columns=['Source', 'RoadTag', 'Slot', 'Classe', 'Descricao', 'Vehicle'])
# print(DF)
# wtrResult.writerow (los['Source'], los['RoadTag'])


# 



# 22|6 - 23|7 - 87|8  (1 sequencia) oksa

# [22,6]
# [23,7]
# [87,8]
# [22,4]
# [23,3]
# [23,4]
# [23,5]
# [87,4]
# [87,6]


# for R, S in [[1,2],[1,4]]:
#     print(R)
#     print(S)
#     res = res[(res["RoadTag"] == R) & (res["Slot"] == S)]
#     for C in [30,50,70]:
#        print(C)





# LOS = res[['ClasseNum','Descricao']].copy()
# LOS.drop_duplicates(subset=None, keep="first", inplace=True)
# LOS=LOS.sort_values(by=['ClasseNum'])

