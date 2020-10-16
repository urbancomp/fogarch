from mpl_toolkits.mplot3d import axes3d

import numpy as np 
import pandas as pd 
import bisect

import matplotlib.pyplot as plt
import csv

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

from sklearn import preprocessing

import plotly.graph_objects as go
import plotly.express as px

import publico as func

pd.options.mode.chained_assignment = None  # default='warn'



ROAD=22
SLOT=6

CONST_TIME_MIN = 0.0
CONST_TIME_MAX = 0.0

EXP="30"
ROAD=22
SLOT=6
TIME_START = 43.0


def MediaPorIntervalor(res_select, interval_time=5):
    global CONST_TIME_MIN
    global CONST_TIME_MAX

    res_select = res_select[res_select['RoadTag']!=0]
    res_select = res_select[(res_select['RoadTag']==ROAD) & (res_select['Slot']==SLOT)]
    res_select.drop_duplicates(subset=None, keep="first", inplace=True)

    # print(CONST_TIME_MIN)
    # print(CONST_TIME_MAX)

    res_select["norm"] = (res_select.STime-CONST_TIME_MIN)/(CONST_TIME_MAX-CONST_TIME_MIN)
    res_select['norm'] = res_select['norm'].map('{:,.1f}'.format)

    return res_select


print("Loading chart...")       

# BASELINE GERAL ***************************************
df1 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
df1['Slot'] = df1['Slot'].astype(int)
df1['Media']  =  df1['Media'].astype(float)
df1['Velo']  =  df1['Velo'].astype(float)
df1['Classe']  =  df1['Classe'].astype(float)
df1['STime']  =  df1['STime'].astype(float)
df1['Timer']  =  df1['Timer'].astype(float)
df1['Source'] = "BASELINE"

df1['Velo'] = df1['Velo'] * 3.6
df1 = df1[df1["STime"] >= TIME_START]
res = df1

# DEFINE OS PARAMETROS QUE OS OUTROS ALGORITMOS DVERÃO SEGUIR
CONST_TIME_MIN = res["STime"].min()
CONST_TIME_MAX = res["STime"].max()

df1_select = MediaPorIntervalor(res)
df1_select = df1_select[['RoadTag','Slot','Source','norm', 'Velo']]

# BASELINE 1TO2 ***************************************
df2 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
df2['Slot'] = df2['Slot'].astype(int)
df2['Media']  =  df2['Media'].astype(float)
df2['Velo']  =  df2['Velo'].astype(float)
df2['Classe']  =  df2['Classe'].astype(float)
df2['STime']  =  df2['STime'].astype(float)
df2['Timer']  =  df2['Timer'].astype(float)
df2['Source'] = "1TO2"

df2['Velo'] = df2['Velo'] * 3.6
df2 = df2[df2["STime"] >= TIME_START]

res = df2
df2_select = MediaPorIntervalor(res)
df2_select = df2_select[['RoadTag','Slot','Source','norm', 'Velo']]

# BASELINE RANDOM ***************************************
df3 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
df3['Slot'] = df3['Slot'].astype(int)
df3['Media']  =  df3['Media'].astype(float)
df3['Velo']  =  df3['Velo'].astype(float)
df3['Classe']  =  df3['Classe'].astype(float)
df3['STime']  =  df3['STime'].astype(float)
df3['Timer']  =  df3['Timer'].astype(float)
df3['Source'] = "RAND"

df3['Velo'] = df3['Velo'] * 3.6
df3 = df3[df3["STime"] >= TIME_START]

res = df3
df3_select = MediaPorIntervalor(res)
df3_select = df3_select[['RoadTag','Slot','Source','norm', 'Velo']]

# BASELINE THRESHOLD ***************************************
df4 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
df4['Slot'] = df4['Slot'].astype(int)
df4['Media']  =  df4['Media'].astype(float)
df4['Velo']  =  df4['Velo'].astype(float)
df4['Classe']  =  df4['Classe'].astype(float)
df4['STime']  =  df4['STime'].astype(float)
df4['Timer']  =  df4['Timer'].astype(float)
df4['Source'] = "LIM-5"

df4['Velo'] = df4['Velo'] * 3.6
df4 = df4[df4["STime"] >= TIME_START]

res = df4
df4_select = MediaPorIntervalor(res)
df4_select = df4_select[['RoadTag','Slot','Source','norm', 'Velo']]


# DBSCAN ***************************************
df5 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
df5['Slot'] = df5['Slot'].astype(int)
df5['Media']  =  df5['Media'].astype(float)
df5['LOS']  =  df5['Classe'].astype(float)
df5['STime']  =  df5['STime'].astype(float)
df5['Timer']  =  df5['Timer'].astype(float)
df5['Clusteres'] =  df5['Clusteres'].astype(int)
df5['Source'] = "DBSCAN"

df5['Velo'] = df5['Velo'] * 3.6
df5 = df5[df5["STime"] >= TIME_START]

res = df5
df5_select = MediaPorIntervalor(res)
df5_select = df5_select[['RoadTag','Slot','Source','norm', 'Velo']]

# XMEANS ***************************************
df7 = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
df7['Slot'] = df7['Slot'].astype(int)
df7['Media']  =  df7['Media'].astype(float)
df7['Media']  =  df7['Media'].astype(float)
df7['LOS']  =  df7['Classe'].astype(float)
df7['STime']  =  df7['STime'].astype(float)
df7['Clusteres'] =  df7['Clusteres'].astype(int)
df7['Source'] = "X-MEANS"

df7['Velo'] = df7['Velo'] * 3.6
df7 = df7[df7["STime"] >= TIME_START]

res = df7
df7_select = MediaPorIntervalor(res)
df7_select = df7_select[['RoadTag','Slot','Source','norm', 'Velo']]

# ******************************************************************************************************

# # ******************************************************************************************************
# res = pd.concat([df1_select, df2_select, df3_select, df4_select, df5_select, df7_select], sort=False) 
# res = pd.concat([df1_select, df5_select, df7_select], sort=False)
res = pd.concat([df1_select, df2_select, df3_select, df4_select], sort=False)

res = res.sort_values(by=['norm','Source'])
res_group = res.groupby(['Source','norm']).mean()

fig = px.line(res_group.reset_index(), x="norm", y="Velo", color="Source").for_each_trace(lambda t: t.update(name=t.name.replace("Source=","")))

# https://plotly.com/python/axes/
# https://plotly.com/python/line-charts/

fig.update_layout(
    # title = "AnaliseAlgorithms ",
    yaxis = dict(
      # range=[0,9],  
      tick0=0, dtick=5,
      title_text='Average Speed (km/h)',
    ),
    font=dict(size=16),
    xaxis = dict(
      title_text='Normalized Simulation Time (<i>t</i>)',
    ),
    # plot_bgcolor='rgba(0,1,0,0)' # 76 # 64
    legend=dict(
      x=0.76,
      y=1.1,
      font=dict(size=16),
      orientation='h'
      ),
      # annotations=[dict(
      #   xref='paper',
      #   yref='paper',
      # )
      # ]
)

fig.show()