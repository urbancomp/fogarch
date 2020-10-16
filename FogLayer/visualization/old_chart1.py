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

EXP="30"
ROAD=22
SLOT=6
        
# BASELINE GERAL ***************************************
df1 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
df1['Slot'] = df1['Slot'].astype(int)
df1['Media']  =  df1['Media'].astype(float)
df1['Velo']  =  df1['Velo'].astype(float)
df1['Classe']  =  df1['Classe'].astype(float)
df1['STime']  =  df1['STime'].astype(float)
df1['Timer']  =  df1['Timer'].astype(float)
df1['Source'] = "BASELINE"

res = df1
res.sort_values(by=['STime'])
df1_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

df1_select = func.MediaPorIntervalor(func.Filter(df1_select,ROAD, SLOT))

# # BASELINE 1TO2 ***************************************
# df2 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
# df2['Slot'] = df2['Slot'].astype(int)
# df2['Media']  =  df2['Media'].astype(float)
# df2['Velo']  =  df2['Velo'].astype(float)
# df2['Classe']  =  df2['Classe'].astype(float)
# df2['STime']  =  df2['STime'].astype(float)
# df2['Timer']  =  df2['Timer'].astype(float)
# df2['Source'] = "BASELINE-1TO2"

# res = df2
# res.sort_values(by=['STime'])
# df2_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

# df2_select = func.MediaPorIntervalor(func.Filter(df2_select,ROAD, SLOT))

# # BASELINE RANDOM ***************************************
# df3 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
# df3['Slot'] = df3['Slot'].astype(int)
# df3['Media']  =  df3['Media'].astype(float)
# df3['Velo']  =  df3['Velo'].astype(float)
# df3['Classe']  =  df3['Classe'].astype(float)
# df3['STime']  =  df3['STime'].astype(float)
# df3['Timer']  =  df3['Timer'].astype(float)
# df3['Source'] = "BASELINE-RANDOM"

# res = df3
# res.sort_values(by=['STime'])
# df3_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

# df3_select = func.MediaPorIntervalor(func.Filter(df3_select,ROAD, SLOT))

# # BASELINE THRESHOLD ***************************************
# df4 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
# df4['Slot'] = df4['Slot'].astype(int)
# df4['Media']  =  df4['Media'].astype(float)
# df4['Velo']  =  df4['Velo'].astype(float)
# df4['Classe']  =  df4['Classe'].astype(float)
# df4['STime']  =  df4['STime'].astype(float)
# df4['Timer']  =  df4['Timer'].astype(float)
# df4['Source'] = "BASELINE-THRESHOLD"

# res = df4
# res.sort_values(by=['STime'])
# df4_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

# df4_select = func.MediaPorIntervalor(func.Filter(df4_select,ROAD, SLOT))

# DBSCAN ***************************************
df5 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
df5['Slot'] = df5['Slot'].astype(int)
df5['Media']  =  df5['Media'].astype(float)
df5['LOS']  =  df5['Classe'].astype(float)
df5['STime']  =  df5['STime'].astype(float)
df5['Timer']  =  df5['Timer'].astype(float)
df5['Clusteres'] =  df5['Clusteres'].astype(int)
df5['Source'] = "DBSCAN"

res = df5
res.sort_values(by=['STime'])
df5_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

df5_select = func.MediaPorIntervalor(func.Filter(df5_select,ROAD, SLOT))

# # DBSCAN FILTER ***************************************
# df6 = pd.read_csv("../repositorio/" + EXP + "/Result_DBSCAN_FILTER.csv") 
# df6['Slot'] = df6['Slot'].astype(int)
# df6['Media']  =  df6['Media'].astype(float)
# df6['LOS']  =  df6['Classe'].astype(float)
# df6['STime']  =  df6['STime'].astype(float)
# df6['Timer']  =  df6['Timer'].astype(float)
# df6['Clusteres'] =  df6['Clusteres'].astype(int)
# df6['Source'] = "DBSCAN - FILTER"

# res = df6
# res.sort_values(by=['STime'])
# df6_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

# df6_select = func.MediaPorIntervalor(func.Filter(df6_select,ROAD, SLOT))

# XMEANS ***************************************
df7 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
df7['Slot'] = df7['Slot'].astype(int)
df7['Media']  =  df7['Media'].astype(float)
df7['Media']  =  df7['Media'].astype(float)
df7['LOS']  =  df7['Classe'].astype(float)
df7['STime']  =  df7['STime'].astype(float)
df7['Clusteres'] =  df7['Clusteres'].astype(int)
df7['Source'] = "X-MEANS"

res = df7
res.sort_values(by=['STime'])
df7_select = res[['RoadTag','Slot','Source','STime', 'Velo']]

df7_select = func.MediaPorIntervalor(func.Filter(df7_select,ROAD, SLOT))

# ******************************************************************************************************
# res = pd.concat([df1_select, df2_select, df3_select, df4_select, df5_select, df6_select, df7_select], sort=False)
# res = pd.concat([df1_select, df5_select, df6_select, df7_select], sort=False)
res = pd.concat([df1_select, df5_select, df7_select], sort=False)


res = res.sort_values(by=['Timer2','Source'])

res_group = res.groupby(['Source','Timer2']).mean()

fig = px.line(res_group.reset_index(), x="Timer2", y="Velo", color="Source", title='XPTO')
fig.show()