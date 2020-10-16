from mpl_toolkits.mplot3d import axes3d

import numpy as np 
import pandas as pd 
import bisect

import matplotlib.pyplot as plt
import csv

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as mtick

from sklearn import preprocessing

import plotly.graph_objects as go
import plotly.express as px

import publico as func

pd.options.mode.chained_assignment = None  # default='warn'


CONST_TIME_MIN = 0.0
CONST_TIME_MAX = 0.0

EXP="z"

# 22|6 - 23|7 - 87|8

ROAD= 87 
SLOT= 8 
TIME_START = 0 #43.0


def MediaPorIntervalor(res_select, interval_time=5):

   
    global CONST_TIME_MIN
    global CONST_TIME_MAX

    res_select = res_select[res_select['RoadTag']!=0]
    res_select = res_select[(res_select['RoadTag']==ROAD) & (res_select['Slot']==SLOT)]
    res_select.drop_duplicates(subset=None, keep="first", inplace=True)

    CONST_TIME_MIN = res_select["STime"].min()
    CONST_TIME_MAX = res_select["STime"].max()

    res_select["norm"] = (res_select.STime-CONST_TIME_MIN)/(CONST_TIME_MAX-CONST_TIME_MIN)
    res_select['norm'] = res_select['norm'].map('{:,.1f}'.format)

    # print(res_select)

    return res_select


print("Loading chart...")       

# BASELINE GERAL ***************************************
baseline = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
baseline['Slot'] = baseline['Slot'].astype(int)
baseline['Media']  =  baseline['Media'].astype(float)
baseline['Velo']  =  baseline['Velo'].astype(float)
baseline['Classe']  =  baseline['Classe'].astype(float)
baseline['STime']  =  baseline['STime'].astype(float)
baseline['Timer']  =  baseline['Timer'].astype(float)
baseline['Source'] = "BASELINE"

baseline['Velo'] = baseline['Velo'] * 3.6
baseline = baseline[baseline["STime"] >= TIME_START]
res = baseline

baseline = MediaPorIntervalor(res)
baseline = baseline[['RoadTag','Slot','Source','norm', 'Velo']]

# 1TO2 ***************************************
oneto2 = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
oneto2['Slot'] = oneto2['Slot'].astype(int)
oneto2['Media']  =  oneto2['Media'].astype(float)
oneto2['Velo']  =  oneto2['Velo'].astype(float)
oneto2['Classe']  =  oneto2['Classe'].astype(float)
oneto2['STime']  =  oneto2['STime'].astype(float)
oneto2['Timer']  =  oneto2['Timer'].astype(float)
oneto2['Source'] = "1TO2"

oneto2['Velo'] = oneto2['Velo'] * 3.6
oneto2 = oneto2[oneto2["STime"] >= TIME_START]

res = oneto2
oneto2 = MediaPorIntervalor(res)
oneto2 = oneto2[['RoadTag','Slot','Source','norm', 'Velo']]

# RANDOM ***************************************
random = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
random['Slot'] = random['Slot'].astype(int)
random['Media']  =  random['Media'].astype(float)
random['Velo']  =  random['Velo'].astype(float)
random['Classe']  =  random['Classe'].astype(float)
random['STime']  =  random['STime'].astype(float)
random['Timer']  =  random['Timer'].astype(float)
random['Source'] = "random"

random['Velo'] = random['Velo'] * 3.6
random = random[random["STime"] >= TIME_START]

res = random
random = MediaPorIntervalor(res)
random = random[['RoadTag','Slot','Source','norm', 'Velo']]

# THRESHOLD ***************************************
limite = pd.read_csv("../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
limite['Slot'] = limite['Slot'].astype(int)
limite['Media']  =  limite['Media'].astype(float)
limite['Velo']  =  limite['Velo'].astype(float)
limite['Classe']  =  limite['Classe'].astype(float)
limite['STime']  =  limite['STime'].astype(float)
limite['Timer']  =  limite['Timer'].astype(float)
limite['Source'] = "LIM-5"

limite['Velo'] = limite['Velo'] * 3.6
limite = limite[limite["STime"] >= TIME_START]

res = limite
limite = MediaPorIntervalor(res)
limite = limite[['RoadTag','Slot','Source','norm', 'Velo']]


# dbscan ***************************************
dbscan = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
dbscan['Slot'] = dbscan['Slot'].astype(int)
dbscan['Media']  =  dbscan['Media'].astype(float)
dbscan['LOS']  =  dbscan['Classe'].astype(float)
dbscan['STime']  =  dbscan['STime'].astype(float)
dbscan['Timer']  =  dbscan['Timer'].astype(float)
dbscan['Clusteres'] =  dbscan['Clusteres'].astype(int)
dbscan['Source'] = "dbscan"

dbscan['Velo'] = dbscan['Velo'] * 3.6
dbscan = dbscan[dbscan["STime"] >= TIME_START]

res = dbscan
dbscan = MediaPorIntervalor(res)
dbscan = dbscan[['RoadTag','Slot','Source','norm', 'Velo']]

# dbscan = dbscan[(dbscan["norm"] < baseline["norm"].max())]


# xmeans ***************************************
xmeans = pd.read_csv("../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
xmeans['Slot'] = xmeans['Slot'].astype(int)
xmeans['Media']  =  xmeans['Media'].astype(float)
xmeans['Media']  =  xmeans['Media'].astype(float)
xmeans['LOS']  =  xmeans['Classe'].astype(float)
xmeans['STime']  =  xmeans['STime'].astype(float)
xmeans['Clusteres'] =  xmeans['Clusteres'].astype(int)
xmeans['Source'] = "X-MEANS"

xmeans['Velo'] = xmeans['Velo'] * 3.6
xmeans = xmeans[xmeans["STime"] >= TIME_START]

res = xmeans
xmeans = MediaPorIntervalor(res)
xmeans = xmeans[['RoadTag','Slot','Source','norm', 'Velo']]

# ******************************************************************************************************

baseline['norm']  =  baseline['norm'].astype(float)
dbscan['norm']  =  dbscan['norm'].astype(float)
oneto2['norm']  =  oneto2['norm'].astype(float)
random['norm']  =  random['norm'].astype(float)
limite['norm']  =  limite['norm'].astype(float)
xmeans['norm']  =  xmeans['norm'].astype(float)


baseline = baseline.groupby(['norm', 'Source']).mean()
oneto2 = oneto2.groupby(['norm', 'Source']).mean()
random = random.groupby(['norm', 'Source']).mean()
limite = limite.groupby(['norm', 'Source']).mean()
dbscan = dbscan.groupby(['norm', 'Source']).mean()
xmeans = xmeans.groupby(['norm', 'Source']).mean()


fig = plt.figure(figsize=(8, 10))
ax = plt.axes()

oneto2.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="1to2", linestyle='solid', marker='+',lw=2.5,ms=12, color="#EF553B")
random.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="Rand", linestyle='solid', marker='*',lw=2.5,ms=12, color="#FFAB6B")
limite.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="Lim", linestyle='solid', marker='v',lw=2.5,ms=12, color="#B57BF9")
dbscan.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="DBSCAN", linestyle='solid', marker='x',lw=2.5,ms=12, color="#00CC96")
xmeans.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="X-Means", linestyle='solid', marker='>',lw=2.5,ms=12, color="#19D3F3")
baseline.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="Baseline", linestyle='solid', marker='s',lw=2.5,ms=12, color="#313997")

ax.set_ylim([0,40])
ax.set_yticks([0, 20, 30, 40])
ax.tick_params(labelsize='28', width=3)

# ax.set_xlim([0,1])
ax.set_xticks([0.0, 0.3,0.6,1.0])

ax.set_ylabel(r"Average Speed (km/h)", labelpad=1,fontsize=28)
ax.set_xlabel(r"Normalized Simulation Time (t)", labelpad=10,fontsize=28)

plt.legend(loc='best', fancybox=False, shadow=False, ncol=2)

plt.setp(plt.gca().get_legend().get_texts(), fontsize='28')

plt.grid( color = "#A6ACAF", linestyle=':', linewidth=0.4)

## HABILITA SO PRA 30 CARROS
# ax.legend().set_visible(False)
# ax.axes.get_yaxis().set_visible(False)

# plt.setp(ax.get_yticklabels(), visible=False) # apafga o eixo em si

plt.savefig('img/TESTE_VELO_COMPOSTO_' + EXP + '_' + str(ROAD) + '_' + str(SLOT) + '.eps', format='eps', dpi=200) 
plt.savefig('img/TESTE_VELO_COMPOSTO_' + EXP + '_' + str(ROAD) + '_' + str(SLOT) + '.png', format='png', dpi=200) 

plt.show()



