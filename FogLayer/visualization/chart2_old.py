from mpl_toolkits.mplot3d import axes3d

import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt
import csv

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

import plotly.graph_objects as go
import plotly.express as px

import publico as func

pd.options.mode.chained_assignment = None  # default='warn'


def SetClasse(value):
    if isinstance(value, float):
        if (value >= 0 and value <= 0.15): return 1 #'Free-flow'
        elif (value > 0.16 and value <= 0.33): return 2 #'Reasonably Free-flow'
        elif (value > 0.33 and value <= 0.50): return 3 #'Stable-flow'
        elif (value > 0.50 and value <= 0.60): return 4 #'Approaching unstable-flow'
        elif (value > 0.60 and value <= 0.70): return 5 #'Unstable-flow'
        elif (value > 0.70 and value <= 1.00): return 6 #'Breakdown-flow'
        else:
            return 'N/A'
    else:
        return str(value)


EXP="30"
ROAD=0 #22
SLOT=0 #6
        
# BASELINE GERAL ***************************************
df1 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
df1['Slot'] = df1['Slot'].astype(int)
df1['Media']  =  df1['Media'].astype(float)
df1['Velo']  =  df1['Velo'].astype(float)
df1['Classe']  =  df1['Classe'].astype(float)
df1['STime']  =  df1['STime'].astype(float)
df1['Timer']  =  df1['Timer'].astype(float)
df1['Source'] = 1

res = df1
res.sort_values(by=['STime'])
df1_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClusterLOS']]

df1_select = func.MediaPorIntervalor(func.Filter(df1_select,ROAD, SLOT))

# # BASELINE 1TO2 ***************************************
# df2 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
# df2['Slot'] = df2['Slot'].astype(int)
# df2['Media']  =  df2['Media'].astype(float)
# df2['Velo']  =  df2['Velo'].astype(float)
# df2['Classe']  =  df2['Classe'].astype(float)
# df2['STime']  =  df2['STime'].astype(float)
# df2['Timer']  =  df2['Timer'].astype(float)
# df2['Source'] = 2

# res = df2
# res.sort_values(by=['STime'])
# df2_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','Clusteres']]

# df2_select = func.MediaPorIntervalor(func.Filter(df2_select,ROAD, SLOT))

# # BASELINE RANDOM ***************************************
# df3 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
# df3['Slot'] = df3['Slot'].astype(int)
# df3['Media']  =  df3['Media'].astype(float)
# df3['Velo']  =  df3['Velo'].astype(float)
# df3['Classe']  =  df3['Classe'].astype(float)
# df3['STime']  =  df3['STime'].astype(float)
# df3['Timer']  =  df3['Timer'].astype(float)
# df3['Source'] = 3

# res = df3
# res.sort_values(by=['STime'])
# df3_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY']]

# df3_select = func.MediaPorIntervalor(func.Filter(df3_select,ROAD, SLOT))

# # BASELINE THRESHOLD ***************************************
# df4 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
# df4['Slot'] = df4['Slot'].astype(int)
# df4['Media']  =  df4['Media'].astype(float)
# df4['Velo']  =  df4['Velo'].astype(float)
# df4['Classe']  =  df4['Classe'].astype(float)
# df4['STime']  =  df4['STime'].astype(float)
# df4['Timer']  =  df4['Timer'].astype(float)
# df4['Source'] = 4

# res = df4
# res.sort_values(by=['STime'])
# df4_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY']]

# df4_select = func.MediaPorIntervalor(func.Filter(df4_select,ROAD, SLOT))

# DBSCAN ***************************************
df5 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
df5['Slot'] = df5['Slot'].astype(int)
df5['Media']  =  df5['Media'].astype(float)
df5['LOS']  =  df5['Classe'].astype(float)
df5['STime']  =  df5['STime'].astype(float)
df5['Timer']  =  df5['Timer'].astype(float)
df5['Clusteres'] =  df5['Clusteres'].astype(int)
df5['Source'] = 5

df5['ClusterLOS'] =  df5['ClusterLOS'].astype(float)

df5['ClusterLOSDesc'] = df5['ClusterLOS'].map(lambda x: SetClasse(x))

res = df5
res.sort_values(by=['STime'])
df5_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClusterLOSDesc']]


print(df5_select)
# df5_select = func.MediaPorIntervalor(func.Filter(df5_select,ROAD, SLOT))

# XMEANS ***************************************
df6 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
df6['Slot'] = df6['Slot'].astype(int)
df6['Media']  =  df6['Media'].astype(float)
df6['Media']  =  df6['Media'].astype(float)
df6['LOS']  =  df6['Classe'].astype(float)
df6['STime']  =  df6['STime'].astype(float)
df6['Clusteres'] =  df6['Clusteres'].astype(int)

df6['Source'] = 6

df6['ClusterLOS'] =  df6['ClusterLOS'].astype(float)

df6['ClusterLOSDesc'] = df6['ClusterLOS'].map(lambda x: SetClasse(x))

res = df6
res.sort_values(by=['STime'])
df6_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClusterLOSDesc']]


# ******************************************************************************************************
# res = pd.concat([df1_select, df2_select, df3_select, df4_select, df5_select, df6_select], sort=False)

res = pd.concat([df6_select], sort=False)

res = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClusterLOSDesc']]


df1_source = res[['Source']]
lista_source = df1_source.values.tolist()

df1_road = res[['RoadTag']]
lista_road = df1_road.values.tolist()

df1_slot = res[['Slot']]
lista_slot = df1_slot.values.tolist()

df1_velo = res[['Velo']]
lista_velo = df1_velo.values.tolist()

# df1_time = res[['Timer2']]
# lista_time = df1_time.values.tolist()

df1_PosX = res[['PosX']]
lista_PosX = df1_PosX.values.tolist()

df1_PosY = res[['PosY']]
lista_PosY = df1_PosY.values.tolist()

df1_Clusteres = res[['ClusterLOSDesc']]
lista_Clusteres = df1_Clusteres.values.tolist()

x = lista_PosX
y = lista_PosY 

# fig=plt.figure()
fig, ax = plt.subplots()


scatter = plt.scatter(x, y, s=lista_velo, marker='+', c=lista_Clusteres)

legend1 = ax.legend(*scatter.legend_elements(), loc="upper left", title="LOS", fancybox=True, shadow=True,)

ax.add_artist(legend1)

# handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
# legend2 = ax.legend(handles, labels, loc="upper left", title="Velocidades")

ax.grid(True)
plt.show()


# # # fig=plt.figure()
# # # ax=fig.add_axes([0,0,1,1])
# # # ax.scatter(lista_source, lista_velo, color='r')
# # # ax.scatter(lista_source, lista_time, color='b')
# # # ax.set_xlabel('Fonte Velo')
# # # ax.set_ylabel('Fonte Tempo')
# # # ax.set_title('scatter plot')
# # # plt.show()