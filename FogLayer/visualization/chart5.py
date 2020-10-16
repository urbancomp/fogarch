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

ROAD=22
SLOT=6

CONST_TIME_MIN = 0.0
CONST_TIME_MAX = 0.0

EXP="70"
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

# DEFINE OS PARAMETROS QUE OS OUTROS ALGORITMOS DVERÃO SEGUIR
CONST_TIME_MIN = res["STime"].min()
CONST_TIME_MAX = res["STime"].max()

baseline = MediaPorIntervalor(res)
baseline = baseline[['RoadTag','Slot','Source','norm', 'Velo']]

# BASELINE 1TO2 ***************************************
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

# BASELINE RANDOM ***************************************
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

# BASELINE THRESHOLD ***************************************
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

baseline = baseline.groupby(['norm', 'Source']).mean()
oneto2 = oneto2.groupby(['norm', 'Source']).mean()
random = random.groupby(['norm', 'Source']).mean()
limite = limite.groupby(['norm', 'Source']).mean()
dbscan = dbscan.groupby(['norm', 'Source']).mean()
xmeans = xmeans.groupby(['norm', 'Source']).mean()

fig = plt.figure(figsize=(10, 8))
ax = plt.axes()


oneto2.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="1TO2", linestyle='solid', marker='+',lw=2.5,ms=12, color="#EF553B")
random.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="Rand", linestyle='solid', marker='*',lw=2.5,ms=12, color="#FFAB6B")
limite.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="LIM-5", linestyle='solid', marker='v',lw=2.5,ms=12, color="#B57BF9")
dbscan.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="DBSCAN", linestyle='solid', marker='x',lw=2.5,ms=12, color="#00CC96")
xmeans.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="XMEANS", linestyle='solid', marker='>',lw=2.5,ms=12, color="#19D3F3")
baseline.reset_index().plot(kind='line',x='norm',y='Velo',ax=ax, label="Baseline", linestyle='solid', marker='s',lw=2.5,ms=12, color="#313997")


ax.set_ylabel(r"Average Speed (km/h)", labelpad=3,fontsize=20)
ax.set_xlabel(r"Normalized Simulation Time (t)", labelpad=10,fontsize=20)

ax.set_ylim([0,40])
ax.tick_params(labelsize='20', width=5)

# fig.axes.get_xaxis().set_visible(False)
# fig.axes.get_yaxis().set_visible(False)

plt.legend(loc='lower right', fancybox=False, shadow=False, ncol=4)

ax.legend().set_visible(False)

plt.setp(plt.gca().get_legend().get_texts(), fontsize='20')

plt.grid( color = "#A6ACAF", linestyle=':', linewidth=0.4)

plt.savefig('img/VELO_TODOS_' + EXP + '.eps', format='eps', dpi=200) 
plt.savefig('img/VELO_TODOS_' + EXP + '.png', format='png', dpi=200) 

# plt.savefig('img/VELO_BASELINES_' + EXP + '.eps', format='eps', dpi=200) 
# plt.savefig('img/VELO_BASELINES_' + EXP + '.png', format='png', dpi=200) 

# plt.savefig('img/VELO_CLUSTERES_' + EXP + '.eps', format='eps', dpi=200) 
# plt.savefig('img/VELO_CLUSTERES_' + EXP + '.png', format='png', dpi=200) 


plt.show()


