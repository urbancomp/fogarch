
from scipy.spatial.distance import cdist
from matplotlib import pyplot as plt
from joblib import dump, load

import numpy as np 
import pandas as pd 

from sklearn.cluster import DBSCAN 
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from random import random

import csv
import config
import os
import time

from beacon import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# utilizado para reproduzir os slots da rua
lenght_via = config.GERAL["lenght_via"]  
interval = config.GERAL["interval"]  

# define o método de redução
send_method = config.GERAL["Configuracao"]  

# caminho local
RemotePathFiles = config.CONSTANTES["RemotePathFiles"]


# reusmos
MEDIA_LOS=0.0
MEDIANA_LOS=0.0

# clusteres
MEDIA_CLUSTER=0.0
MEDIA_RUIDO=0.0
COUNT_CLUSTERES=0
COUNT_RUIDO=0
COUNT_DATA = 0

# Sporte aos Tipos de baseline
BASELINE1TO2=0
BASELINETHRESHOLD=5.0

# arquivo final
SIZE_FINAL_FILE=0.0

# datasets de suporte
DF_PREVIOUS=pd.DataFrame()
LS_DATA =[]

START_TIME = time.time()


# Limpa arquivos da pasta data antes de iniciar o serviço
def ClearFolder(folder):
    listfodler = os.listdir(folder)
    for item in listfodler: 
        if item.endswith(".csv") or item.endswith(".zip"):
            os.remove(os.path.join(folder + item)) 

# Converte um Array em um CSV
def ArrrayToCSV(myArray, csvFilePath, clusters, cluster_los=0.0):    
    header=True
    media_velo=0.0
    total_velo=0.0
    count=0
    config.CountCluster+=1

    if (os.path.exists(csvFilePath)):
        header=False

    wtr = csv.writer(open (csvFilePath, 'a'), delimiter=',', lineterminator='\n')
    if (header):
        wtr.writerow (['Cut','Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot','Media'])
    
    for item in myArray:

        count+=1
        total_velo = total_velo + float(item[2])
        media_velo = (total_velo /  count)
        wtr.writerow ([config.CountCluster, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8],media_velo])
        
        # Replica o conteúdo impressono arquivo para calculo de acurácia lol
        GeralFile.append([config.CountCluster, item[8], item[1], item[3], item[4], item[5], item[6], item[7], item[2],1,0.0,0.0,"", clusters, cluster_los])
        
        
    del wtr
    
    # print("\nArquivo gravado: " + csvFilePath + "\n")    

# Executa o método de análise definido no arquivo config.py
def DataAnalyseMethod(oBeacons):

    global MEDIA_CLUSTER
    global COUNT_CLUSTERES
    global COUNT_RUIDO
    global COUNT_DATA
    global BASELINE1TO2
    global BASELINETHRESHOLD
    global DF_PREVIOUS
    global LS_DATA
    global START_TIME
    

    # Agrupa dados para deifnir o trafego em cada slot da pista 
    if (send_method==1): 

        df = pd.DataFrame(np.asarray([oBeacons]), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])
        df['Velo'] = df['Velo'].astype(float)
        df['Id'] = df['Id'].astype(int)
        df['STime'] = df['STime'].astype(float)

        COUNT_CLUSTERES = 0
        COUNT_RUIDO = 0
        COUNT_DATA += len(df.index)

        ArrrayToCSV(df.to_numpy(), RemotePathFiles + 'BASELINE_ALL.csv',0) # caminho para medir o desemoenho da rede
 
    elif (send_method==2):  # DBSCAN: Retorna % de elementos de cada cluster
            
        ELAPSED_TIME = (oBeacons[7] - START_TIME)
        # print("Tempo decorrido ", ELAPSED_TIME)
        # print("Tamanho do dataset", str(len(LS_DATA)))

        if (ELAPSED_TIME < 10): # Se não alcancou o tempo decorrido, coleta dados
            print("Constuíndo...", ELAPSED_TIME)
            LS_DATA.append(oBeacons)

        else: # Ao alcançaer o tepo decorrido, processa os dados    
            print("Processando...")
            START_TIME = oBeacons[7]    
            
            df = pd.DataFrame(np.asarray(LS_DATA), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])
            df['Velo'] = df['Velo'].astype(float)
            df['Id'] = df['Id'].astype(int)
            df['QtdCar'] = df[['Id']].count(axis=1)
            df['STime'] = df['STime'].astype(float)

            # Recorte dos dados para dbscan
            data = df.iloc[:,4:6] # Pos XY

            db = DBSCAN(eps=40, min_samples=3).fit(data)
            core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
            core_samples_mask[db.core_sample_indices_] = True
            labels = db.labels_

            # Grava os dados em um aruqivo para realizar o monitoramento dos clusteres em outro processo.
            pd.DataFrame(data).to_csv("dataview/data.csv", index=False)

            # Number of clusters in labels, ignoring noise if present.
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)
            
            COUNT_CLUSTERES = COUNT_CLUSTERES + n_clusters_
            COUNT_RUIDO = COUNT_RUIDO + n_noise_
            COUNT_DATA += len(data.index)

            pd.options.display.max_columns = None
            pd.options.display.max_rows = None
        
            # print('Clusters: %d' % n_clusters_)
            # print('Ruído: %d' % n_noise_)

            percent = 0.3 # capturar 30% dos dados de cada cluster
            for c in (set(filter(lambda r: r != -1,list(labels)))): 
                ArrrayToCSV(df[labels==c].sample(n=(max(int(round(len(df[labels==c])*percent)),1))).to_numpy(),RemotePathFiles + 'DBSCAN_PART.csv', n_clusters_) 

            LS_DATA.clear()
            LS_DATA.append(oBeacons)

    elif (send_method==3):  # DBSCAN: Retorna apenas o primeiro exemplar de cada cluster

        df = pd.DataFrame(np.asarray(oBeacons), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])

        df['Velo'] = df['Velo'].astype(float)
        df['Id'] = df['Id'].astype(int)
        df['QtdCar'] = df[['Id']].count(axis=1)
        df['STime'] = df['STime'].astype(float)

        data = df.iloc[:,4:6]
        db = DBSCAN(eps=40, min_samples=3).fit(data)
        labels = db.labels_
        
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise_ = list(labels).count(-1)

        # print("\n+++++++++++++++++++++\n")
        # print(df)
        # print("\n+++++++++++++++++++++\n")

        # print("Clusters: " + str(n_clusters_) + " Ruido: " + str(n_noise_))
        # print(labels)

        COUNT_CLUSTERES = COUNT_CLUSTERES + n_clusters_
        COUNT_RUIDO = COUNT_RUIDO + n_noise_
        COUNT_DATA += len(data.index)

        pd.options.display.max_columns = None
        pd.options.display.max_rows = None        
        
        amostra=[]
        if (n_clusters_>0):
            for c in (set(filter(lambda r: r != -1,list(labels)))): 
                idx=0
                for value in labels:
                    if (value == c):
                        amostra.append(df.iloc[idx])
                        config.Temp=df.iloc[idx]
                        break
                    idx+=1  
            ArrrayToCSV(amostra, RemotePathFiles + 'DBSCAN_FILTER.csv', n_clusters_)

        # else:
        #     if (len(config.Temp)>0):
        #         # print("Sem formação de Cluster: Replicando o ultimo registro")
        #         amostra.append(config.Temp)
        #         ArrrayToCSV(amostra, RemotePathFiles + 'DBSCAN_FILTER.csv',n_clusters_)

    elif (send_method==4): # xMeans: Retorna os dados do cluster mais proximo do centroide utilizando o xmeans

        ELAPSED_TIME = (oBeacons[7] - START_TIME)

        if (ELAPSED_TIME < 7): # Se não alcancou o tempo decorrido, coleta dados
            print("Constuíndo...", ELAPSED_TIME)
            LS_DATA.append(oBeacons)

        else: # Ao alcançaer o tepo decorrido, processa os dados    
            
            print("Processando...")
            START_TIME = oBeacons[7]    

            df = pd.DataFrame(np.asarray(LS_DATA), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])

            df['Velo'] = df['Velo'].astype(float)
            df['Id'] = df['Id'].astype(int)
            df['QtdCar'] = df[['Id']].count(axis=1)
            df['STime'] = df['STime'].astype(float)

            df['PosX'] = df['PosX'].astype(float)
            df['PosY'] = df['PosY'].astype(float)

        
            # data_select = df.iloc[:,[3, 4,5]] # Pos XY
            data_select = df.iloc[:,[4,5]] 
            data = np.asarray(data_select).tolist()
            
            pd.DataFrame(data).to_csv("dataview/data.csv", index=False)

            initial_centers = kmeans_plusplus_initializer(data, 2).initialize() # kmenas inicia com uam pesuqsia por 2 clusteres
            instances = xmeans(data, initial_centers, criterion = 1, ccore=False) # aplica o xmeans executando os clusteres
            instances.process()

            # local_wce = instances.get_total_wce()
            clusters = instances.get_clusters()
            centers = instances.get_centers()

            # Escolher o elemento mais próximo do centroide 
            i=0
            min_dist = 10000000000 
            min_label=0
            amostra=[]

            cluster_velo_total=0.0
            cluster_velo_media=0.0
            cluster_los = 0.0
            cont_elem=0

            for c in clusters:
                # print("\n\n*** loop centros****")
                # print(centers[i])
                # print("******************\n\n")
                cluster_velo_total=0.0
                cluster_velo_media=0.0
                cluster_los = 0.0
                cont_elem=1
                
                # Localiza o centroid mais próximo
                for lbl in c:
                    isExist= False
                    # print("\n\n***testando elementos***")
                    # print(lbl)
                    # print("*******************\n\n")
                    
                    mean_distance = [np.sqrt((x-centers[i][0])**2+(y-centers[i][1])**2) for x, y in np.nditer(data[lbl])]
                    
                    # print("Teste Distância")
                    # print(mean_distance[0])
                    if (min_dist>=mean_distance[0]):
                        # print("Essa é menor")
                        min_dist = mean_distance[0]
                        min_label = lbl
                i+=1 
                
                # verifica se o registro foi enviado na ultima iteração
                amostra.append(df.iloc[min_label])

            ArrrayToCSV(amostra,RemotePathFiles + 'XMEANS_CENTER.csv', 0,0)


            # # xmenas retornando percentual do cluster
            # percent = 0.3 # capturar 30% dos dados de cada cluster
            # # Obtem um percentual dos clusteres formados
            # for c in clusters:
            #     ArrrayToCSV(df.loc[(c)].sample(n=(max(int(len(c)*percent),1))).to_numpy(),RemotePathFiles + 'XMEANS_CENTER.csv', 0,0) 

            # LS_DATA.clear()
            # LS_DATA.append(oBeacons)

    elif (send_method==5):  # BASELINE 1/2
        
        df = pd.DataFrame(np.asarray([oBeacons]), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])
        df['Velo'] = df['Velo'].astype(float)
        df['Id'] = df['Id'].astype(int)
        df['STime'] = df['STime'].astype(float)

        if (BASELINE1TO2==3):
            BASELINE1TO2=0
        elif(BASELINE1TO2>0):
            COUNT_CLUSTERES = 0
            COUNT_RUIDO = 0
            COUNT_DATA += len(df.index)            
            ArrrayToCSV(df.to_numpy(), RemotePathFiles + 'BASELINE_1TO2.csv',0) 


        BASELINE1TO2+=1
            
    elif (send_method==6):  # BASELINE RANDOM
        
        df = pd.DataFrame(np.asarray([oBeacons]), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])
        df['Velo'] = df['Velo'].astype(float)
        df['Id'] = df['Id'].astype(int)
        df['STime'] = df['STime'].astype(float)
    
        if (random() < 0.5):
            COUNT_CLUSTERES = 0
            COUNT_RUIDO = 0
            COUNT_DATA += len(df.index)
            ArrrayToCSV(df.to_numpy(), RemotePathFiles + 'BASELINE_RANDOM.csv',0) 


        BASELINE1TO2+=1

    elif (send_method==7):  # BASELINE LIMITES
        
        df = pd.DataFrame(np.asarray([oBeacons]), columns=['Header', 'Id', 'Velo', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Slot'])
        print('tamanho original: ' +  str(df.size))

        df['Velo'] = df['Velo'].astype(float)
        df['Id'] = df['Id'].astype(int)
        df['STime'] = df['STime'].astype(float)

        df_threshold = df[df['Velo'] > BASELINETHRESHOLD]
        print('tamanho final: ' +  str(df_threshold.size))

        ArrrayToCSV(df_threshold.to_numpy(), RemotePathFiles + 'BASELINE_THRESHOLD.csv',0) 

GeralFile=[]

def GenerateLogFilePorEstrada():

    print("\n\n**** Analisando por Estrada***\n\n")

    global MEDIA_LOS
    global MEDIANA_LOS
    
    dfLog = pd.DataFrame(np.asarray(GeralFile), columns=['Cut', 'Slot', 'Id', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Velo','QtdBcn','Media', 'Classe' ,'Descricao', 'Clusteres','ClusterLOS'])
    
    dfLog['Cut'] = dfLog['Cut'].astype(int)
    dfLog['Slot'] = dfLog['Slot'].astype(int)
    dfLog['Velo'] = dfLog['Velo'].astype(float)
    dfLog['Media'] = dfLog['Media'].astype(float)
    dfLog['Classe'] = dfLog['Classe'].astype(float)
    dfLog['STime'] = dfLog['STime'].astype(float)
    dfLog['QtdBcn'] = dfLog['QtdBcn'].astype(int)
    dfLog['ClusterLOS'] = dfLog['ClusterLOS'].astype(float)

    dfLog['RoadTag'] = dfLog.Road.str[:2] # Marca o prefixo das ruas, nomalmente ste prefixo pode ser atribuido a toda a rua

    dfLog = dfLog.sort_values(by =['Road', 'Slot', 'STime'])

    media_velo = 0.0
    velo_total=0.0
    count=0
    previousTime=0.0
    ElapsedTime = 0.0
    MaxSlot = int(dfLog['Slot'].max())
    minimo = int(dfLog['Slot'].min())
    cut=0
    velo_max = float(dfLog['Velo'].max())

    ListRoads = dfLog['Road'].unique().tolist()

    for road in ListRoads: 

        # print("\\n\nESTRADA: " + road + "\n\n")    
        SLOTS = dfLog.loc[(dfLog.Road==road)]
        MaxSlot = int(SLOTS['Slot'].max())
        minimo = int(SLOTS['Slot'].min())   

        velo_max = float(SLOTS['Velo'].max())  # coloquei -7 para deixar o transito mais livre no LOS
        
        for idx in range(minimo, MaxSlot+1):  

            print("Analisando Slots: " + str(idx) + " Estrada:" + road)
            
            # a cada seção sera tudo
            previousTime=0.0
            velo_total = 0.0
            count=0 
            cut=0

            # filtra pelo slot
            DFFilter = dfLog.loc[(dfLog.Slot == idx) & (dfLog.Road==road)]

            # itera dentor do slot aplicando calculos a cada x'ts
            for index, row in DFFilter.iterrows():

                # Esta rotina serve apenas para demardcar intervalos de 5 segundo nos registro baseado no tempo de simulação
                if previousTime == 0: previousTime = row['STime']
                ElapsedTime = ((row['STime']) - (previousTime))

                # Controla o tempo, zerando o contador a cada 0.5 segundos de tempo de simulação
                if (ElapsedTime > 0.5): 
                    # print("Corte temporal")
                    
                    # tempo limite alcançado - reinicia a contagem
                    previousTime=0.0
                    velo_total = 0.0
                    count=0 
                    cut=0

                else:
                    previousTime = row['STime'] 
                    cut+=1 # corte temporal, marca no aruqivo os registro referentes a cada grupo/tempo de simulação

                # marca o corte temporal
                dfLog.at[index,"Cut"] = cut                

                # Calcula media
                velo_total = velo_total + row['Velo']
                count+=1
            
                # if (count==0):count=1

                media_velo = velo_total / count
                dfLog.at[index,"Media"] = media_velo    
            
                # calcula los
                dfLog.at[index,"Classe"] =  ((velo_max - media_velo) / velo_max)    
                dfLog.at[index,"Descricao"] =  SetClasse(((velo_max - media_velo) / velo_max))


    MEDIA_LOS =  dfLog["Classe"].mean()
    MEDIANA_LOS =  dfLog["Classe"].median()

    print("meida los: " + str(MEDIA_LOS))
    print("mediana lod: " + str(MEDIANA_LOS))

    descfile=""
    if (send_method==1):
        descfile = "Result_LOS_GERAL.csv"
    elif (send_method==2):
        descfile = "Result_LOS_DBSCAN.csv"
    elif (send_method==3):
        descfile = "Result_DBSCAN_FILTER.csv"
    elif (send_method==4):
        descfile = "Result_LOS_XMEANS.csv"
    elif (send_method==5):
        descfile = "Result_BASELINE_1TO2.csv"
    elif (send_method==6):
        descfile = "Result_BASELINE_RANDOM.csv"
    elif (send_method==7):
        descfile = "Result_BASELINE_THRESHOLD.csv"
    else:
        descfile = "Result_OUTRO.csv"

    if not os.path.isfile('log/' + descfile):
        dfLog.to_csv("log/" + descfile, mode='a', index=False)
    else:
        dfLog.to_csv("log/" + descfile, mode='a', index=False, header=False)


def GenerateLogFilePorSlot():
    
    print("\n\n**** Analisando por Slots***\n\n")

    global MEDIA_LOS
    global MEDIANA_LOS
    
    dfLog = pd.DataFrame(np.asarray(GeralFile), columns=['Cut', 'Slot', 'Id', 'Road', 'PosX', 'PosY', 'STime', 'Timer', 'Velo','QtdBcn','Media', 'Classe' ,'Descricao', 'Clusteres'])
    
    dfLog['Cut'] = dfLog['Cut'].astype(int)
    dfLog['Slot'] = dfLog['Slot'].astype(int)
    dfLog['Velo'] = dfLog['Velo'].astype(float)
    dfLog['Media'] = dfLog['Media'].astype(float)
    dfLog['Classe'] = dfLog['Classe'].astype(float)
    dfLog['STime'] = dfLog['STime'].astype(float)
    dfLog['QtdBcn'] = dfLog['QtdBcn'].astype(int)

    dfLog['RoadTag'] = dfLog.Road.str[:2] # Marca o prefixo das ruas, nomalmente ste prefixo pode ser atribuido a toda a rua


    dfLog = dfLog.sort_values(by =['Slot', 'STime'])

    media_velo = 0.0
    velo_total=0.0
    count=0
    previousTime=0.0
    ElapsedTime = 0.0
    MaxSlot = int(dfLog['Slot'].max())
    minimo = int(dfLog['Slot'].min())
    cut=0

    for idx in range(minimo, MaxSlot+1):  

        print("Analisando Slots: " + str(idx))
        
        # a cada seção sera tudo
        previousTime=0.0
        velo_total = 0.0
        count=0 
        cut=0

        # filtra pelo slot
        DFFilter = dfLog.loc[(dfLog.Slot == idx)]

        # itera dentor do slot aplicando calculos a cada x'ts
        for index, row in DFFilter.iterrows():

            # Esta rotina serve apenas para demardcar intervalos de 5 segundo nos registro baseado no tempo de simulação
            if previousTime == 0: previousTime = row['STime']
            ElapsedTime = ((row['STime']) - (previousTime))

            # Controla o tempo, zerando o contador a cada 0.5 segundos de tempo de simulação
            if (ElapsedTime > 0.5): 
                # print("Corte temporal")
                
                # tempo limite alcançado - reinicia a contagem
                previousTime=0.0
                velo_total = 0.0
                count=0 
                cut=0

            else:
                previousTime = row['STime'] 
                cut+=1 # corte temporal, marca no aruqivo os registro referentes a cada grupo/tempo de simulação

            # marca o corte temporal
            dfLog.at[index,"Cut"] = cut                

            # Calcula media
            velo_total = velo_total + row['Velo']
            count+=1
            media_velo = velo_total / count
            dfLog.at[index,"Media"] = media_velo    
            
            # calcula los
            dfLog.at[index,"Classe"] =  ((80 - media_velo) / 80)    
            dfLog.at[index,"Descricao"] =  SetClasse(((80 - media_velo) / 80))

        

    MEDIA_LOS =  dfLog["Classe"].mean()
    MEDIANA_LOS =  dfLog["Classe"].median()

    print("meida los: " + str(MEDIA_LOS))
    print("mediana lod: " + str(MEDIANA_LOS))

    descfile=""
    if (send_method==1):
        descfile = "Result_LOS_GERAL_POR_SLOT.csv"
    elif (send_method==2):
        descfile = "Result_LOS_DBSCAN_POR_SLOT.csv"
    elif (send_method==3):
        descfile = "Result_DBSCAN_FILTER_POR_SLOT.csv"
    elif (send_method==4):
        descfile = "Result_LOS_XMEANS_POR_SLOT.csv"
    elif (send_method==5):
        descfile = "Result_BASELINE_1TO2_POR_SLOT.csv"
    elif (send_method==6):
        descfile = "Result_BASELINE_RANDOM_POR_SLOT.csv"
    elif (send_method==7):
        descfile = "Result_BASELINE_THRESHOLD_POR_SLOT.csv"
    else:
        descfile = "Result_OUTRO.csv"

    if not os.path.isfile('log/' + descfile):
        dfLog.to_csv("log/" + descfile, mode='a', index=False)
    else:
        dfLog.to_csv("log/" + descfile, mode='a', index=False, header=False)


def SetClasse(value):
    if isinstance(value, float):
        if (value >= 0 and value <= 0.15): return 'Free-flow'
        elif (value > 0.16 and value <= 0.33): return 'Reasonably Free-flow'
        elif (value > 0.33 and value <= 0.50): return 'Stable-flow'
        elif (value > 0.50 and value <= 0.60): return 'Approaching unstable-flow'
        elif (value > 0.60 and value <= 0.70): return 'Unstable-flow'
        elif (value > 0.70 and value <= 1.00): return 'Breakdown-flow'
        else:
            return 'Free-flow'
    else:
        return str(value)


def PrintResumo():
    # Imprime Resumo do Experimento

    if (COUNT_DATA >0): MEDIA_CLUSTER = COUNT_CLUSTERES /  COUNT_DATA
    if (COUNT_DATA >0): MEDIA_RUIDO = COUNT_RUIDO /  COUNT_DATA
    
    print(chr(27) + "[2J")
    print("\n\n\n\n")
    print("***** RESUMO *****")
    print("\n\n")
    print("Media LOS: " + str(MEDIA_LOS))
    print("Mediana LOS: " + str(MEDIANA_LOS))
    print("Media de clusteres criados: " + str(MEDIA_CLUSTER))
    print("Media de ruidos : " + str(MEDIA_RUIDO))
    print("\n\n")




   