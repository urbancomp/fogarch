import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics

from plotly.offline import download_plotlyjs, plot,iplot
import cufflinks as cf

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


baseline = pd.read_csv("../repositorio/30_v2/Result_LOS_GERAL.csv")
baseline['Slot'] = baseline['Slot'].astype(int)
baseline['Media']  =  baseline['Media'].astype(float)
baseline['Velo']  =  baseline['Velo'].astype(float)
baseline['Classe']  =  baseline['Classe'].astype(float)
baseline['STime']  =  baseline['STime'].astype(float)
baseline['Timer']  =  baseline['Timer'].astype(float)
baseline['Source'] = "BASELINE"

dbscan = pd.read_csv("../repositorio/30_v2/Result_LOS_DBSCAN.csv")
dbscan['Slot'] = dbscan['Slot'].astype(int)
dbscan['Media']  =  dbscan['Media'].astype(float)
dbscan['Velo']  =  dbscan['Velo'].astype(float)
dbscan['Classe']  =  dbscan['Classe'].astype(float)
dbscan['STime']  =  dbscan['STime'].astype(float)
dbscan['Timer']  =  dbscan['Timer'].astype(float)
dbscan['Source'] = "DBSCAN"

xmeans = pd.read_csv("../repositorio/30_v2/Result_LOS_XMEANS.csv")
xmeans['Slot'] = xmeans['Slot'].astype(int)
xmeans['Media']  =  xmeans['Media'].astype(float)
xmeans['Velo']  =  xmeans['Velo'].astype(float)
xmeans['Classe']  =  xmeans['Classe'].astype(float)
xmeans['STime']  =  xmeans['STime'].astype(float)
xmeans['Timer']  =  xmeans['Timer'].astype(float)
xmeans['Source'] = "XMEANS"


oneto2 = pd.read_csv("../repositorio/30_v2/Result_BASELINE_1TO2.csv")
oneto2['Slot'] = oneto2['Slot'].astype(int)
oneto2['Media']  =  oneto2['Media'].astype(float)
oneto2['Velo']  =  oneto2['Velo'].astype(float)
oneto2['Classe']  =  oneto2['Classe'].astype(float)
oneto2['STime']  =  oneto2['STime'].astype(float)
oneto2['Timer']  =  oneto2['Timer'].astype(float)
oneto2['Source'] = "1TO2"

random = pd.read_csv("../repositorio/30_v2/Result_BASELINE_RANDOM.csv")
random['Slot'] = random['Slot'].astype(int)
random['Media']  =  random['Media'].astype(float)
random['Velo']  =  random['Velo'].astype(float)
random['Classe']  =  random['Classe'].astype(float)
random['STime']  =  random['STime'].astype(float)
random['Timer']  =  random['Timer'].astype(float)
random['Source'] = "RANDOM"

limite = pd.read_csv("../repositorio/30_v2/Result_BASELINE_THRESHOLD.csv")
limite['Slot'] = limite['Slot'].astype(int)
limite['Media']  =  limite['Media'].astype(float)
limite['Velo']  =  limite['Velo'].astype(float)
limite['Classe']  =  limite['Classe'].astype(float)
limite['STime']  =  limite['STime'].astype(float)
limite['Timer']  =  limite['Timer'].astype(float)
limite['Source'] = "LIMITE"

result = pd.concat([baseline,dbscan, xmeans, oneto2, random, limite], sort=False)

data = result[['Source','Road','Slot','Classe']]

# Substitui 0 to NAN
data['Classe'] = data['Classe'].replace({0:np.nan})

# Define um pivot table e deifne faltantes como None
pivot = data.pivot_table(index=['Road','Slot'], columns='Source' , values = 'Classe', aggfunc='mean', fill_value=0)

# Arquivo sem imputação de dados
pd.DataFrame(pivot.reset_index()).to_csv("dataviewteste_dados_fantando.csv", index=False)

# # Imputação de dados
new_dbscan = pivot.reset_index()[['DBSCAN']].interpolate(method ='akima', limit_direction ='both') 
pivot['DBSCAN'] = new_dbscan['DBSCAN'].values

new_xmeans = pivot.reset_index()[['XMEANS']].interpolate(method ='linear', limit_direction ='both')  
pivot['XMEANS'] = new_xmeans['XMEANS'].values

new_1to2 = pivot.reset_index()[['1TO2']].interpolate(method ='linear', limit_direction ='both')  
pivot['1TO2'] = new_1to2['1TO2'].values

new_random = pivot.reset_index()[['RANDOM']].interpolate(method ='linear', limit_direction ='both')  
pivot['RANDOM'] = new_random['RANDOM'].values

new_limite = pivot.reset_index()[['LIMITE']].interpolate(method ='linear', limit_direction ='both')  
pivot['LIMITE'] = new_limite['LIMITE'].values

# calculo do erro com tolerancia de 0.1
pivot['ERR_DBSCAN'] = np.isclose(pivot['BASELINE'], pivot['DBSCAN'], atol=0.1, equal_nan=False)
pivot['ERR_XMEANS'] = np.isclose(pivot['BASELINE'], pivot['XMEANS'], atol=0.1, equal_nan=False)
pivot['ERR_1TO2'] =   np.isclose(pivot['BASELINE'], pivot['1TO2'],   atol=0.1, equal_nan=False)
pivot['ERR_RAND'] =   np.isclose(pivot['BASELINE'], pivot['RANDOM'], atol=0.1, equal_nan=False)
pivot['ERR_LIMITE'] = np.isclose(pivot['BASELINE'], pivot['LIMITE'], atol=0.1, equal_nan=False)

algoritmos = pivot[["BASELINE", "DBSCAN", "XMEANS", "1TO2", "RANDOM", "LIMITE"]]
erros = pivot[["ERR_DBSCAN", "ERR_XMEANS", "ERR_1TO2", "ERR_RAND", "ERR_LIMITE"]]


# VISUALIZAÇÕES ---

## Tentativa de encontrar relação entre o aumento da quantidade de registro e pontos de los mais altos
# data2 = result[['Source','Descricao','Classe','Id']]
# data2['Descricao'][data2['Descricao']=='Free-flow']=1
# data2['Descricao'][data2['Descricao']=='Reasonably Free-flow']=2
# data2['Descricao'][data2['Descricao']=='Stable-flow']=3
# data2['Descricao'][data2['Descricao']=='Approaching unstable-flow']=4
# data2['Descricao'][data2['Descricao']=='Unstable-flow']=5
# data2['Descricao'][data2['Descricao']=='Breakdown-flow']=6
# data3 = data2.groupby(['Source','Descricao','Classe']).count()
# datafinal = data3.reset_index() 
# fig, (ax1) = plt.subplots(ncols=3,nrows=2)
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='BASELINE'] , ax=ax1[0,0])
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='DBSCAN']   , ax=ax1[0,1])
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='XMEANS']   , ax=ax1[0,2])
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='1TO2']     , ax=ax1[1,0])
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='RANDOM']   , ax=ax1[1,1])
# sns.regplot(x='Id', y='Descricao', data=datafinal[datafinal['Source']=='LIMITE']   , ax=ax1[1,2])
# plt.show()

#-------------------------------------------------------------------

# Distribuição por algoritmo
# data2 = data[['Source','Classe']]
# sns.stripplot(x='Source',y='Classe', data=data2, jitter=True)
# plt.show()

#-------------------------------------------------------------------

# # Erros (isclosery: True | False)
ax = plt.axes()
sns.heatmap(erros, cmap='RdYlGn', fmt=".1f", cbar_kws={
                                                'ticks': [0, 1],
                                            },
            ) 
ax.set_title('Acurácia por valores aproximados: Tolerância de 0.1')
plt.show()

#-------------------------------------------------------------------

# Dados dos Algoritmos
# ax = plt.axes()
# sns.heatmap(algoritmos, cmap='coolwarm', fmt=".1f") 
# ax.set_title('Algoritmos x Valores de LOS')
# plt.show()

#-------------------------------------------------------------------

# # Coorelação entre algoritmos
# sns.heatmap(algoritmos.corr(), cmap='coolwarm')
# plt.show()

#-------------------------------------------------------------------

# # Coorelação geraç
# algoritmos.reset_index()['DBSCAN'].hist()
# plt.show()


# Define um Dataframe com os erros

df = pd.DataFrame()
COLUNAS = [
    'Metric',
    'Algorithm',
    'Value'
]

from collections import OrderedDict
MAE = OrderedDict(
{
'Metric': ['MAE','MAE','MAE','MAE','MAE'],
'Algorithm': ['DBSCAN','XMEANS','1TO2','RANDOM','LIMITE'],
'Value': [  metrics.mean_absolute_error(pivot['BASELINE'], pivot['DBSCAN']),
            metrics.mean_absolute_error(pivot['BASELINE'], pivot['XMEANS']), 
            metrics.mean_absolute_error(pivot['BASELINE'], pivot['1TO2']), 
            metrics.mean_absolute_error(pivot['BASELINE'], pivot['RANDOM']),
            metrics.mean_absolute_error(pivot['BASELINE'], pivot['LIMITE']),
]})

MSE = OrderedDict(
{
'Metric': ['MSE','MSE','MSE','MSE','MSE'],
'Algorithm': ['DBSCAN','XMEANS','1TO2','RANDOM','LIMITE'],
'Value': [  metrics.mean_squared_error(pivot['BASELINE'], pivot['DBSCAN']),
            metrics.mean_squared_error(pivot['BASELINE'], pivot['XMEANS']), 
            metrics.mean_squared_error(pivot['BASELINE'], pivot['1TO2']), 
            metrics.mean_squared_error(pivot['BASELINE'], pivot['RANDOM']),
            metrics.mean_squared_error(pivot['BASELINE'], pivot['LIMITE']),
]})

RSME = OrderedDict(
{
'Metric': ['RSME','RSME','RSME','RSME','RSME'],
'Algorithm': ['DBSCAN','XMEANS','1TO2','RANDOM','LIMITE'],
'Value': [  np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['DBSCAN'])),
            np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['XMEANS'])), 
            np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['1TO2'])), 
            np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['RANDOM'])),
            np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['LIMITE'])),
]})

APTOL = OrderedDict(
{
'Metric': ['APTOL','APTOL','APTOL','APTOL','APTOL'],
'Algorithm': ['DBSCAN','XMEANS','1TO2','RANDOM','LIMITE'],
'Value': [  (len(pivot[pivot['ERR_DBSCAN'] == True]) / len(pivot)) *100,
            (len(pivot[pivot['ERR_XMEANS'] == True]) / len(pivot)) *100, 
            (len(pivot[pivot['ERR_1TO2'] == True]) / len(pivot)) *100, 
            (len(pivot[pivot['ERR_RAND'] == True]) / len(pivot)) *100,
            (len(pivot[pivot['ERR_LIMITE'] == True]) / len(pivot)) *100,
]})


df_MAE = pd.DataFrame(MAE)
df_MSE = pd.DataFrame(MSE)
df_RSME = pd.DataFrame(RSME)
df_APTOL = pd.DataFrame(APTOL)

# ------------------------------------------------------------------

fig, ax = plt.subplots(nrows=2,ncols=2)
sns.barplot(x='Algorithm', y='Value', data=df_MAE, ax=ax[0][0] )
sns.barplot(x='Algorithm', y='Value', data=df_MSE, ax=ax[0][1] )
sns.barplot(x='Algorithm', y='Value', data=df_RSME, ax=ax[1][0] )
sns.barplot(x='Algorithm', y='Value', data=df_APTOL, ax=ax[1][1] )

ax[0][0].set_title("MAE")
ax[0][1].set_title("MSE")
ax[1][0].set_title("RMSE")
ax[1][1].set_title("ACURACIA DIF/TOLERÂNCIA (0.1) ")
plt.show()

# ------------------------------------------------------------------

# fig, ax  = plt.subplots(ncols=1,nrows=1)

# x = ['BASELINE','DBSCAN','XMEANS','1TO2','RANDOM','LIMITE']
# y = [len(baseline),len(dbscan),len(xmeans),len(oneto2),len(random),len(limite)]
# ax.bar(x,y)
# ax.set_title("Quantidade de Registros")
# plt.show()

# print(len(baseline))
# print(len(dbscan))
# print(len(xmeans))
# print(len(oneto2))
# print(len(random))
# print(len(limite))

# ------------------------------------------------------------------

print("** MEAN ABSOLUTE ERROR (MAE) **")
print("DBSCAN: ", metrics.mean_absolute_error(pivot['BASELINE'], pivot['DBSCAN']))
print("XMEANS: ", metrics.mean_absolute_error(pivot['BASELINE'], pivot['XMEANS']))
print("1TO2:   ", metrics.mean_absolute_error(pivot['BASELINE'], pivot['1TO2']))
print("RANDOM: ", metrics.mean_absolute_error(pivot['BASELINE'], pivot['RANDOM']))
print("LIMITE: ", metrics.mean_absolute_error(pivot['BASELINE'], pivot['LIMITE']))
print("\n")

print("** MEAN SQUARED ERROR (MSE) **")
print("DBSCAN: ", metrics.mean_squared_error(pivot['BASELINE'], pivot['DBSCAN']))
print("XMEANS: ", metrics.mean_squared_error(pivot['BASELINE'], pivot['XMEANS']))
print("1TO2:   ", metrics.mean_squared_error(pivot['BASELINE'], pivot['1TO2']))
print("RANDOM: ", metrics.mean_squared_error(pivot['BASELINE'], pivot['RANDOM']))
print("LIMITE: ", metrics.mean_squared_error(pivot['BASELINE'], pivot['LIMITE']))
print("\n")

print("** Root Mean Square Error (RSME) **")
print("DBSCAN: ", np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['DBSCAN'])))
print("XMEANS: ", np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['XMEANS'])))
print("1TO2:   ", np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['1TO2'])))
print("RANDOM: ", np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['RANDOM'])))
print("LIMITE: ", np.sqrt(metrics.mean_squared_error(pivot['BASELINE'], pivot['LIMITE'])))
print("\n")

print("** Diferença - Tolerância de 0.1 **")
acuracy_dbscan = (len(pivot[pivot['ERR_DBSCAN'] == True]) / len(pivot)) *100
acuracy_xmeans = (len(pivot[pivot['ERR_XMEANS'] == True]) / len(pivot)) *100
acuracy_1to2 = (len(pivot[pivot['ERR_1TO2'] == True]) / len(pivot)) *100
acuracy_rand = (len(pivot[pivot['ERR_RAND'] == True]) / len(pivot)) *100
acuracy_limite = (len(pivot[pivot['ERR_LIMITE'] == True]) / len(pivot)) *100
print("Acuracy dbscan: ", acuracy_dbscan)
print("Acuracy xmeans: ", acuracy_xmeans)
print("Acuracy 1 to 2: ", acuracy_1to2)
print("Acuracy random: ", acuracy_rand)
print("Acuracy limite: ", acuracy_limite)

## Grava aruqivo
pd.DataFrame(pivot.reset_index()).to_csv("dataviewteste.csv", index=False)








## EXEMPLOS DE METRICAS PARA INSERÇAO DE DADOS FALTANTES
# new_dbscan = pivot.reset_index()[['DBSCAN']].interpolate(method ='linear', limit_direction ='both') 
# new_dbscan = pivot.reset_index()[['DBSCAN']].interpolate(method='spline', order=2, limit_direction ='both') 
# new_dbscan = pivot.reset_index()[['DBSCAN']].fillna(method='bfill')
# new_dbscan = pivot.reset_index()[['DBSCAN']].interpolate(method ='cubic', limit_direction ='both')  
# new_dbscan = pivot.reset_index()[['DBSCAN']].bfill().ffill() 

# Organizando colunas
# from pandas.api.types import CategoricalDtype
# data['Source']=data['Source'].astype(CategoricalDtype(categories=[
#                                                                     "BASELINE", 
#                                                                     "DBSCAN", 
#                                                                     "ERR_DBSCAN", 
#                                                                     "XMEANS", 
#                                                                     "ERR_XMEANS", 
#                                                                     "1TO2", 
#                                                                     "ERR_1TO2", 
#                                                                     "RANDOM", 
#                                                                     "ERR_RAND", 
#                                                                     "LIMITE", 
#                                                                     "ERR_LIMITE"]
#                                                         )
#                                     )