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

from dateutil import parser


def MediaFileRede(res_select, interval_time=5):
        
    res_select.drop_duplicates(subset=None, keep="first", inplace=True)

    # cria campos
    res_select['Timer2']  =  0
    res_select['Media2']  =  0.0    

    velo_total = 0.0
    count=0 
    timer_atual = 0.0
    timer_ant = 0.0
    elapset_atual= 0.0
    elapset_cumulativo = 0.0

    count_timer=interval_time

    for index, row in res_select.iterrows():
        
        timer_atual  = row['STime']

        if (timer_ant!=0.0): 
            elapset_atual = float(row['STime']) - float(timer_ant)
            
            # print(abs(elapset_atual))
            
            elapset_cumulativo+=float(elapset_atual)
            
            if ((elapset_cumulativo >= interval_time)): 
                # print('Chegou')
                # break
                media_velo = velo_total / count
                res_select.at[index,"Media2"] = media_velo 
                res_select.at[index,"Timer2"] = count_timer
                
                elapset_cumulativo=0.0
                timer_ant = 0.0
                velo_total=0.0
                media_velo=0.0
                count=0

                count_timer+=interval_time

        if (timer_atual != timer_ant):
            timer_ant = timer_atual

        velo_total = velo_total + row['Bytes']
        count+=1
    
    
    # remove zeros
    res_select = res_select[res_select['Timer2']!=0]
    return res_select

EXP="30"
        
print("Loading Dataframe...")
# BASELINE GERAL ***************************************************
df1 = pd.read_csv("../repositorio/" + EXP + "/REDE_GERAL.csv")

df1['Download']  =  df1['Download'].astype(float)
df1['Upload']  =  df1['Upload'].astype(float)
df1['Duracao']  =  df1['Duracao'].astype(float)
df1['STime']  =  df1['STime'].astype(float)
df1['Bytes']  =  df1['Bytes'].astype(float)
df1['Source'] = "BASELINE"

df1_filtro = df1.loc[(df1['Bytes'] > 0)]
df1_select = df1_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
df1_select = MediaFileRede(df1_select)
# *************************************************************************
print("Loading Dataframe...")

# # BASELINE 1TO 2 **********************************************************
# df2 = pd.read_csv("../repositorio/" + EXP + "/REDE_BASELINE_1TO2.csv")

# df2['Download']  =  df2['Download'].astype(float)
# df2['Upload']  =  df2['Upload'].astype(float)
# df2['Duracao']  =  df2['Duracao'].astype(float)
# df2['STime']  =  df2['STime'].astype(float)
# df2['Bytes']  =  df2['Bytes'].astype(float)
# df2['Source'] = "BASELINE - 1TO2"


# df2_filtro = df2.loc[(df2['Bytes'] > 0)]
# df2_select = df2_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
# df2_select = MediaFileRede(df2_select)
# #********************************************************************
# print("Loading Dataframe...")

# # BASELINE RANDOM **********************************************************
# df3 = pd.read_csv("../repositorio/" + EXP + "/REDE_BASELINE_RANDOM.csv")

# df3['Download']  =  df3['Download'].astype(float)
# df3['Upload']  =  df3['Upload'].astype(float)
# df3['Duracao']  =  df3['Duracao'].astype(float)
# df3['STime']  =  df3['STime'].astype(float)
# df3['Bytes']  =  df3['Bytes'].astype(float)
# df3['Source'] = "BASELINE - RANDOM"


# df3_filtro = df3.loc[(df3['Bytes'] > 0)]
# df3_select = df3_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
# df3_select = MediaFileRede(df3_select)
# #********************************************************************
# print("Loading Dataframe...")

# # BASELINE THRESHOLD **********************************************************
# df4 = pd.read_csv("../repositorio/" + EXP + "/REDE_BASELINE_THRESHOLD.csv")

# df4['Download']  =  df4['Download'].astype(float)
# df4['Upload']  =  df4['Upload'].astype(float)
# df4['Duracao']  =  df4['Duracao'].astype(float)
# df4['STime']  =  df4['STime'].astype(float)
# df4['Bytes']  =  df4['Bytes'].astype(float)
# df4['Source'] = "BASELINE - THRESHOLD"


# df4_filtro = df4.loc[(df4['Bytes'] > 0)]
# df4_select = df4_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
# df4_select = MediaFileRede(df4_select)
# #********************************************************************
print("Loading Dataframe...")

# DBSCAN **********************************************************
df5 = pd.read_csv("../repositorio/" + EXP + "/REDE_DBSCAN.csv")

df5['Download']  =  df5['Download'].astype(float)
df5['Upload']  =  df5['Upload'].astype(float)
df5['Duracao']  =  df5['Duracao'].astype(float)
df5['STime']  =  df5['STime'].astype(float)
df5['Bytes']  =  df5['Bytes'].astype(float)
df5['Source'] = "DBSCAN"

df5_filtro = df5.loc[(df5['Bytes'] > 0)]
df5_select = df5_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
df5_select = MediaFileRede(df5_select)
#********************************************************************
print("Loading Dataframe...")

# # DBSCAN FILTER  **********************************************************
# df6 = pd.read_csv("../repositorio/" + EXP + "/REDE_DBSCAN_FILTER.csv")

# df6['Download']  =  df6['Download'].astype(float)
# df6['Upload']  =  df6['Upload'].astype(float)
# df6['Duracao']  =  df6['Duracao'].astype(float)
# df6['STime']  =  df6['STime'].astype(float)
# df6['Bytes']  =  df6['Bytes'].astype(float)
# df6['Source'] = "DBSCAN - FILTER"

# df6_filtro = df6.loc[(df6['Bytes'] > 0)]
# df6_select = df6_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
# df6_select = MediaFileRede(df6_select)
# #********************************************************************

# XMEANS **********************************************************
df7 = pd.read_csv("../repositorio/" + EXP + "/REDE_XMEANS.csv")

df7['Download']  =  df7['Download'].astype(float)
df7['Upload']  =  df7['Upload'].astype(float)
df7['Duracao']  =  df7['Duracao'].astype(float)
df7['STime']  =  df7['STime'].astype(float)
df7['Bytes']  =  df7['Bytes'].astype(float)
df7['Source'] = "XMEANS"


df7_filtro = df7.loc[(df7['Bytes'] > 0)]
df7_select = df7_filtro[['Upload','Bytes','Source', 'STime','Duracao']]
df7_select = MediaFileRede(df7_select)
#********************************************************************
print("Loading Chart...")

# res = pd.concat([df1_select, df2_select, df3_select, df4_select, df5_select, df7_select], sort=False)
# res = pd.concat([df1_select, df2_select, df3_select, df4_select, df5_select, df6_select, df7_select], sort=False)
res = pd.concat([df1_select, df5_select, df7_select], sort=False)

res.sort_values(by=['Timer2','Source'])


fig = px.line(res, x="Timer2", y="Media2", color="Source", title='XPTO')
fig.show()


# res_group = res.groupby(['Source']).mean()



# fig = px.line(res_group.reset_index(), x="Timer2", y="Media2", color="Source", title='XPTO')
# fig.show()
