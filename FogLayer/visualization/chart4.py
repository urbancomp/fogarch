from mpl_toolkits.mplot3d import axes3d

import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt
import csv

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

import plotly.graph_objects as go
import plotly.express as px

import publico as func

pd.options.mode.chained_assignment = None  # default='warn'

from dateutil import parser

def MediaFileRede(res_select, interval_time=5):
        
    res_select.drop_duplicates(subset=None, keep="first", inplace=True)
    
    # # cria campos
    # res_select['Timer2']  =  0
    # res_select['Media2']  =  0.0    

    # velo_total = 0.0
    # count=0 
    # timer_atual = 0.0
    # timer_ant = 0.0
    # elapset_atual= 0.0
    # elapset_cumulativo = 0.0

    # count_timer=interval_time

    # for index, row in res_select.iterrows():
        
    #     timer_atual  = row['Tempo']

    #     if (timer_ant!=0.0): 
    #         elapset_atual = float(row['Tempo']) - float(timer_ant)
            
    #         # print(abs(elapset_atual))
            
    #         elapset_cumulativo+=float(elapset_atual)
            
    #         if ((elapset_cumulativo >= interval_time)): 
    #             # print('Chegou')
    #             # break
    #             media_velo = velo_total / count
    #             res_select.at[index,"Media2"] = media_velo 
    #             res_select.at[index,"Timer2"] = count_timer
                
    #             elapset_cumulativo=0.0
    #             timer_ant = 0.0
    #             velo_total=0.0
    #             media_velo=0.0
    #             count=0

    #             count_timer+=interval_time

    #     if (timer_atual != timer_ant):
    #         timer_ant = timer_atual

    #     velo_total = velo_total + row['Download']
    #     count+=1
    
    
    # remove zeros
    # res_select = res_select[(res_select['Timer2']!=0) & (res_select['Timer2']<=280) & (res_select['Media2']<300) ]
    
    return res_select

EXP30="30"
EXP50="50"
EXP70="70"
        
print("Loading Dataframe...")
# BASELINE 30 ***************************************************
baseline_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_GERAL.csv")

baseline_30['Download']  =  baseline_30['Download'].astype(float)
baseline_30['Upload']  =  baseline_30['Upload'].astype(float)
baseline_30['Tempo']  =  baseline_30['Tempo'].astype(float)
baseline_30['Source'] = "BASELINE"
baseline_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
baseline_30_select = baseline_30[['Download', 'Source', 'Tempo', 'Carros']]
baseline_30_select = MediaFileRede(baseline_30_select)
# *************************************************************************

# BASELINE 50 ***************************************************
baseline_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_GERAL.csv")

baseline_50['Download']  =  baseline_50['Download'].astype(float)
baseline_50['Upload']  =  baseline_50['Upload'].astype(float)
baseline_50['Tempo']  =  baseline_50['Tempo'].astype(float)
baseline_50['Source'] = "BASELINE"
baseline_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
baseline_50_select = baseline_50[['Download', 'Source', 'Tempo', 'Carros']]
baseline_50_select = MediaFileRede(baseline_50_select)
# *************************************************************************

# BASELINE 70 ***************************************************
baseline_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_GERAL.csv")

baseline_70['Download']  =  baseline_70['Download'].astype(float)
baseline_70['Upload']  =  baseline_70['Upload'].astype(float)
baseline_70['Tempo']  =  baseline_70['Tempo'].astype(float)
baseline_70['Source'] = "BASELINE"
baseline_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
baseline_70_select = baseline_70[['Download', 'Source', 'Tempo', 'Carros']]
baseline_70_select = MediaFileRede(baseline_70_select)
# *************************************************************************

baseline = res = pd.concat([baseline_30_select,baseline_50_select,baseline_70_select], sort=False)

#
#
#

# ONETO2 30 ***************************************************
oneTo2_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_BASELINE_1TO2.csv")

oneTo2_30['Download']  =  oneTo2_30['Download'].astype(float)
oneTo2_30['Upload']  =  oneTo2_30['Upload'].astype(float)
oneTo2_30['Tempo']  =  oneTo2_30['Tempo'].astype(float)
oneTo2_30['Source'] = "1to2"
oneTo2_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
oneTo2_30_select = oneTo2_30[['Download', 'Source', 'Tempo', 'Carros']]
oneTo2_30_select = MediaFileRede(oneTo2_30_select)
# *************************************************************************

# ONETO2 50 ***************************************************
oneTo2_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_BASELINE_1TO2.csv")

oneTo2_50['Download']  =  oneTo2_50['Download'].astype(float)
oneTo2_50['Upload']  =  oneTo2_50['Upload'].astype(float)
oneTo2_50['Tempo']  =  oneTo2_50['Tempo'].astype(float)
oneTo2_50['Source'] = "1to2"
oneTo2_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
oneTo2_50_select = oneTo2_50[['Download', 'Source', 'Tempo', 'Carros']]
oneTo2_50_select = MediaFileRede(oneTo2_50_select)
# *************************************************************************

# 1TO2 70 ***************************************************
oneTo2_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_BASELINE_1TO2.csv")

oneTo2_70['Download']  =  oneTo2_70['Download'].astype(float)
oneTo2_70['Upload']  =  oneTo2_70['Upload'].astype(float)
oneTo2_70['Tempo']  =  oneTo2_70['Tempo'].astype(float)
oneTo2_70['Source'] = "1to2"
oneTo2_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
oneTo2_70_select = oneTo2_70[['Download', 'Source', 'Tempo', 'Carros']]
oneTo2_70_select = MediaFileRede(oneTo2_70_select)
# *************************************************************************

oneTo2 = res = pd.concat([oneTo2_30_select,oneTo2_50_select,oneTo2_70_select], sort=False)

#
#
#

# RANDOM 30 ***************************************************
random_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_BASELINE_RANDOM.csv")

random_30['Download']  =  random_30['Download'].astype(float)
random_30['Upload']  =  random_30['Upload'].astype(float)
random_30['Tempo']  =  random_30['Tempo'].astype(float)
random_30['Source'] = "Rand"
random_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
random_30_select = random_30[['Download', 'Source', 'Tempo', 'Carros']]
random_30_select = MediaFileRede(random_30_select)
# *************************************************************************

# RANDOM 50 ***************************************************
random_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_BASELINE_RANDOM.csv")

random_50['Download']  =  random_50['Download'].astype(float)
random_50['Upload']  =  random_50['Upload'].astype(float)
random_50['Tempo']  =  random_50['Tempo'].astype(float)
random_50['Source'] = "Rand"
random_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
random_50_select = random_50[['Download', 'Source', 'Tempo', 'Carros']]
random_50_select = MediaFileRede(random_50_select)
# *************************************************************************

# RANDOM 70 ***************************************************
random_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_BASELINE_RANDOM.csv")

random_70['Download']  =  random_70['Download'].astype(float)
random_70['Upload']  =  random_70['Upload'].astype(float)
random_70['Tempo']  =  random_70['Tempo'].astype(float)
random_70['Source'] = "Rand"
random_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
random_70_select = random_70[['Download', 'Source', 'Tempo', 'Carros']]
random_70_select = MediaFileRede(random_70_select)
# *************************************************************************

random = res = pd.concat([random_30_select,random_50_select,random_70_select], sort=False)

#
#
#

# LIMITE 30 ***************************************************
limite_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_BASELINE_THRESHOLD.csv")

limite_30['Download']  =  limite_30['Download'].astype(float)
limite_30['Upload']  =  limite_30['Upload'].astype(float)
limite_30['Tempo']  =  limite_30['Tempo'].astype(float)
limite_30['Source'] = "Lim"
limite_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
limite_30_select = limite_30[['Download', 'Source', 'Tempo', 'Carros']]
limite_30_select = MediaFileRede(limite_30_select)
# *************************************************************************

# LIMITE 50 ***************************************************
limite_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_BASELINE_THRESHOLD.csv")

limite_50['Download']  =  limite_50['Download'].astype(float)
limite_50['Upload']  =  limite_50['Upload'].astype(float)
limite_50['Tempo']  =  limite_50['Tempo'].astype(float)
limite_50['Source'] = "Lim"
limite_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
limite_50_select = limite_50[['Download', 'Source', 'Tempo', 'Carros']]
limite_50_select = MediaFileRede(limite_50_select)
# *************************************************************************

# LIMITE 70 ***************************************************
limite_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_BASELINE_THRESHOLD.csv")

limite_70['Download']  =  limite_70['Download'].astype(float)
limite_70['Upload']  =  limite_70['Upload'].astype(float)
limite_70['Tempo']  =  limite_70['Tempo'].astype(float)
limite_70['Source'] = "Lim"
limite_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
limite_70_select = limite_70[['Download', 'Source', 'Tempo', 'Carros']]
limite_70_select = MediaFileRede(limite_70_select)
# *************************************************************************

limite = res = pd.concat([limite_30_select,limite_50_select,limite_70_select], sort=False)

#
#
#

# DBSCAN 30  ***************************************************
dbscan_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_DBSCAN.csv")

dbscan_30['Download']  =  dbscan_30['Download'].astype(float)
dbscan_30['Upload']  =  dbscan_30['Upload'].astype(float)
dbscan_30['Tempo']  =  dbscan_30['Tempo'].astype(float)
dbscan_30['Source'] = "DNSCAN"
dbscan_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
dbscan_30_select = dbscan_30[['Download', 'Source', 'Tempo', 'Carros']]
dbscan_30_select = MediaFileRede(dbscan_30_select)
# *************************************************************************

# BASELINE DBSCAN 50  ***************************************************
dbscan_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_DBSCAN.csv")

dbscan_50['Download']  =  dbscan_50['Download'].astype(float)
dbscan_50['Upload']  =  dbscan_50['Upload'].astype(float)
dbscan_50['Tempo']  =  dbscan_50['Tempo'].astype(float)
dbscan_50['Source'] = "DNSCAN"
dbscan_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
dbscan_50_select = dbscan_50[['Download', 'Source', 'Tempo', 'Carros']]
dbscan_50_select = MediaFileRede(dbscan_50_select)
# *************************************************************************


# DBSCAN 70  ***************************************************
dbscan_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_DBSCAN.csv")

dbscan_70['Download']  =  dbscan_70['Download'].astype(float)
dbscan_70['Upload']  =  dbscan_70['Upload'].astype(float)
dbscan_70['Tempo']  =  dbscan_70['Tempo'].astype(float)
dbscan_70['Source'] = "DNSCAN"
dbscan_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
dbscan_70_select = dbscan_70[['Download', 'Source', 'Tempo', 'Carros']]
dbscan_70_select = MediaFileRede(dbscan_70_select)
# *************************************************************************

dbscan = res = pd.concat([dbscan_30_select,dbscan_50_select,dbscan_70_select], sort=False)

#
#
#

# XMEANS 30  ***************************************************
xmeans_30 = pd.read_csv("../repositorio/" + EXP30 + "/REDE_XMEANS.csv")

xmeans_30['Download']  =  xmeans_30['Download'].astype(float)
xmeans_30['Upload']  =  xmeans_30['Upload'].astype(float)
xmeans_30['Tempo']  =  xmeans_30['Tempo'].astype(float)
xmeans_30['Source'] = "X-Means"
xmeans_30['Carros'] = 30

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
xmeans_30_select = xmeans_30[['Download', 'Source', 'Tempo', 'Carros']]
xmeans_30_select = MediaFileRede(xmeans_30_select)
# *************************************************************************

# XMEANS 50  ***************************************************
xmeans_50 = pd.read_csv("../repositorio/" + EXP50 + "/REDE_XMEANS.csv")

xmeans_50['Download']  =  xmeans_50['Download'].astype(float)
xmeans_50['Upload']  =  xmeans_50['Upload'].astype(float)
xmeans_50['Tempo']  =  xmeans_50['Tempo'].astype(float)
xmeans_50['Source'] = "X-Means"
xmeans_50['Carros'] = 50

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
xmeans_50_select = xmeans_50[['Download', 'Source', 'Tempo', 'Carros']]
xmeans_50_select = MediaFileRede(xmeans_50_select)
# *************************************************************************

# XMEANS xmeans 70  ***************************************************
xmeans_70 = pd.read_csv("../repositorio/" + EXP70 + "/REDE_XMEANS.csv")

xmeans_70['Download']  =  xmeans_70['Download'].astype(float)
xmeans_70['Upload']  =  xmeans_70['Upload'].astype(float)
xmeans_70['Tempo']  =  xmeans_70['Tempo'].astype(float)
xmeans_70['Source'] = "X-Means"
xmeans_70['Carros'] = 70

# df1_filtro = df1.loc[(df1['Bytes'] > 0)]
xmeans_70_select = xmeans_70[['Download', 'Source', 'Tempo', 'Carros']]
xmeans_70_select = MediaFileRede(xmeans_70_select)
# *************************************************************************

xmeans = res = pd.concat([xmeans_30_select,xmeans_50_select,xmeans_70_select], sort=False)

#
#
#

print("Loading Chart...")

Geral = res = pd.concat([baseline,oneTo2,random,limite,dbscan,xmeans], sort=False)

# AGRUPAMENTOS
baseline = baseline.groupby(['Source', 'Carros']).mean()
oneTo2 = oneTo2.groupby(['Source', 'Carros']).mean()
random = random.groupby(['Source', 'Carros']).mean()
limite = limite.groupby(['Source', 'Carros']).mean()
dbscan = dbscan.groupby(['Source', 'Carros']).mean()
xmeans = xmeans.groupby(['Source', 'Carros']).mean()


# CMVERTE EM %
# baseline['Percent'] = (baseline['Download']/Geral['Download'].sum() *100) 
# oneTo2['Percent'] = (oneTo2['Download']/Geral['Download'].sum() *100)
# random['Percent'] = (random['Download']/Geral['Download'].sum() *100)
# limite['Percent'] = (limite['Download']/Geral['Download'].sum() *100)
# dbscan['Percent'] = (dbscan['Download']/Geral['Download'].sum() *100)
# xmeans['Percent'] = (xmeans['Download']/Geral['Download'].sum() *100)

# .value_counts(normalize=True) * 100

baseline['Norm'] = (baseline['Download']/Geral['Download'].sum()) 
oneTo2['Norm'] = (oneTo2['Download']/Geral['Download'].sum() )
random['Norm'] = (random['Download']/Geral['Download'].sum() )
limite['Norm'] = (limite['Download']/Geral['Download'].sum() )
dbscan['Norm'] = (dbscan['Download']/Geral['Download'].sum() )
xmeans['Norm'] = (xmeans['Download']/Geral['Download'].sum() )

Geral = res = pd.concat([baseline,oneTo2,random,limite,dbscan,xmeans], sort=False)

baseline['Percent'] = (baseline['Norm']/Geral['Norm'].max()-0.2) *100
oneTo2['Percent'] = (oneTo2['Norm']/Geral['Norm'].max()-0.2) *100
random['Percent'] = (random['Norm']/Geral['Norm'].max()-0.2) *100
limite['Percent'] = (limite['Norm']/Geral['Norm'].max()-0.2) *100
dbscan['Percent'] = (dbscan['Norm']/Geral['Norm'].max()-0.2) *100
xmeans['Percent'] = (xmeans['Norm']/Geral['Norm'].max()-0.15) *100

# print(baseline)
# print(oneTo2)
# print(random)
# print(limite)
# print(dbscan)
# print(xmeans)


# baseline['Percent'] = baseline.Percent / baseline.Percent.sum() *100
# oneTo2['Percent'] = oneTo2.Percent / oneTo2.Percent.sum() *100
# random['Percent'] = random.Percent / random.Percent.sum() *100
# limite['Percent'] = limite.Percent / limite.Percent.sum() *100
# dbscan['Percent'] = dbscan.Percent / dbscan.Percent.sum() *100
# xmeans['Percent'] = xmeans.Percent / xmeans.Percent.sum() *100


fig = plt.figure(figsize=(10, 8))
ax = plt.axes()

# PLOTAGEM
oneTo2.reset_index().plot(kind='line',x='Carros',y='Percent',ax=ax, label="1to2", linestyle=':', marker='+',lw=2.5,ms=12, color="#EF553B")
random.reset_index().plot(kind='line',x='Carros',y='Percent',ax=ax, label="Rand", linestyle=':', marker='*',lw=2.5,ms=12, color="#FFAB6B")
limite.reset_index().plot(kind='line',x='Carros',y='Percent',ax=ax, label="Lim", linestyle=':', marker='v',lw=2.5,ms=12, color="#B57BF9")
dbscan.reset_index().plot(kind='line',x='Carros',y='Percent',  ax=ax, label="DBSCAN",   linestyle=':', marker='X',lw=2.5,ms=12, color="#00CC96")
xmeans.reset_index().plot(kind='line',x='Carros',y='Percent',  ax=ax, label="X-Means",   linestyle=':', marker='>',lw=2.5,ms=12, color="#19D3F3")
baseline.reset_index().plot(kind='line',x='Carros',y='Percent',ax=ax, label="Baseline", linestyle=':', marker='s',lw=2.5,ms=12, color="#313997")

ax.set_xticks([30,50,70])
ax.set_ylim([0,100])
ax.tick_params(labelsize='20', width=5)

fmt = '%.0f%%'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)

ax.set_ylabel(r"Network Usage (%)", labelpad=2,fontsize=20)
ax.set_xlabel(r"Number of Vehicles", labelpad=10,fontsize=20)

# plt.xlabel('Number of Vehicles')
# plt.ylabel('Network Usage (%)')

plt.legend(loc='upper center', fancybox=False, shadow=False, ncol=4)

plt.setp(plt.gca().get_legend().get_texts(), fontsize='20')

plt.grid( color = "#A6ACAF", linestyle=':', linewidth=0.4)

plt.savefig('img/REDE_GERAL.eps', format='eps', dpi=200) 
plt.savefig('img/REDE_GERAL.png', format='png', dpi=200) 

plt.show()

