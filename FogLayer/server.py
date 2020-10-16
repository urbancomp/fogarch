import numpy as np 
import pandas as pd 
from sklearn.cluster import DBSCAN 

import bisect
import config
import threading
import time
import socket
from beacon import *
from functools import reduce

from datetime import datetime
from analyse import *
from receiver import *

import psutil
import datetime


# Variáveis da aplicaçaõ
AllBeacons = []
Cars = []
HashCode=[]
RoadFilter = config.GERAL["RoadFilter"]  

IsRun = True
STime=0
total_bytes = 0


#Exclui aruqivos gerados em outra execução
#ClearFolder(RemotePathFiles)
ClearFolder("datasource/")
ClearFolder("dataview/")
ClearFolder("log/")
ClearFolder("data/")
ClearFolder("net/")


wtr = csv.writer(open ("datasource/AllBeacons.csv", 'a'), delimiter=',', lineterminator='\n')
wtr.writerow (['Header','Id','Velo','Road','PosX','PosY','STime', 'Timer', 'Slot'])

# **** Monitoramento de Dados de Rede
def Monitor():

    global IsRun
    global STime
    
    # define o método de redução
    send_method = config.GERAL["Configuracao"]  

    count=0

    global total_bytes 

    ul=0.0
    dl=0.0
    t0 = time.time()

    upload=psutil.net_io_counters(pernic=True)['wlp3s0'][0]
    download=psutil.net_io_counters(pernic=True)['wlp3s0'][1] 
    up_down=(upload,download)
    

    if (send_method==1):
        descfile = "net/REDE_GERAL.csv"
    elif (send_method==2):
        descfile = "net/REDE_DBSCAN.csv"
    elif (send_method==3):
        descfile = "net/REDE_DBSCAN_FILTER.csv"
    elif (send_method==4):
        descfile = "net/REDE_XMEANS.csv"
    elif (send_method==5):
        descfile = "net/REDE_BASELINE_1TO2.csv"
    elif (send_method==6):
        descfile = "net/REDE_BASELINE_RANDOM.csv"        
    elif (send_method==7):
        descfile = "net/REDE_BASELINE_THRESHOLD.csv"        


    wtr = csv.writer(open (descfile, 'a'), delimiter=',', lineterminator='\n')
    wtr.writerow (['Download','Upload', 'STime', 'Duracao','Bytes'])

    while IsRun:
        
        last_up_down = up_down
        upload=psutil.net_io_counters(pernic=True)['wlp3s0'][0]
        download=psutil.net_io_counters(pernic=True)['wlp3s0'][1]
        t1 = time.time()
        up_down = (upload,download)
        
        
        total_bytes = total_bytes + ((upload - last_up_down[0])/1024)

        try:
            ul, dl = [(now - last) / (t1 - t0) / 1024.0 for now,last in zip(up_down, last_up_down)]             
            t0 = time.time()
            
        except:
            pass

        if (dl>0.1 or ul>=0.1):
            time.sleep(1) 
            # print("aguarde...")
            #os.system('ls')

        # print('UL: {:0.2f} kB/s \n'.format(ul)+'DL: {:0.2f} kB/s'.format(dl))
        # print('UL: {:0.2f} kB/s \n'.format(ul))
        # if (raio_prev != raio):
        #     raio_prev=raio
        #     count=0

        # mão grava valores 0
        # if (ul>0.1):
        #     count+=1
        #     wtr.writerow ([0.0, ul,STime,raio,total_bytes])
        
        count+=1
        wtr.writerow ([0.0, ul,STime, 0, total_bytes])

    print("thread Finalizada!")   

t = threading.Thread(target=ReceiveSocketData)
t.start()

# Inicializa a thread de monitoramnto de rede
# m = threading.Thread(target=Monitor)
# m.start()

prev_size = 0
size=0
idx=0

try:

    while True:

        time.sleep(0.005)
        size = len(DataReciver)

        if (idx < size-1):
        
            row = DataReciver[idx]
            # print(row)

            Header = row[0]
            Id     = row[1].split(":")[1]
            Velo   = float(row[2].split(":")[1])
            Road   = row[3].split(":")[1]
            # Road  = Road[:(100 if (Road.find('#')==-1) else Road.find('#'))]
            # Road = (Road.replace('-','') if (Road.isnumeric()) else  0)

            PosX   = float(row[4].split(":")[1])
            PosY   = float(row[5].split(":")[1])

            PosRoad   = float(row[6].split(":")[1])
            LenRoad   = float(row[7].split(":")[1])

            STime  = float(row[8].split(":")[1])  
            Timer  = time.time()

            # Pega a posição x e define o s5lot apropriado 
            idxSlot    = bisect.bisect_left(range(0,int(LenRoad),5), PosRoad) 
            Slot   = idxSlot


            # print("\n\n-------\n\n")
            # print(str(Road)[0:2])
            # print(str(RoadFilter[0]))
            # print(str(RoadFilter[1]))
            # print("\n\n-------\n\n")
            
            if (len(RoadFilter) != 0):
                if((str(Road)[0:2] != RoadFilter[0]) and str(Road)[0:2] != RoadFilter[1]):
                    # print("Remove")
                    idx+=1
                    continue

            #cria objeto beacon
            oBeacon = Beacon(Header,Id,Velo,Road,PosX,PosY,STime, Timer, Slot)

            # # lista que armazena todos os beacons recebidos (suporte)
            AllBeacons.append(oBeacon)

            wtr.writerow ([Header,Id,Velo,Road,PosX,PosY,STime, Timer, Slot])

            # Obtem o carro e altera os dados (removiodo em: 16062020 )
            # isExist = list(filter(lambda car: car[1] == Id, Cars))
            # if len(isExist)==0 :
            #     Cars.append([Header,Id,Velo,Road,PosX,PosY,STime, Timer, Slot])
            # else:
            #     idxCar = Cars.index(isExist[0])
            #     Cars[idxCar][2]  = Velo
            #     Cars[idxCar][3]  = Road
            #     Cars[idxCar][4]  = PosX
            #     Cars[idxCar][5]  = PosY
            #     Cars[idxCar][6]  = STime
            #     Cars[idxCar][7]  = Timer
            #     Cars[idxCar][8]  = Slot 
            # print(Cars)

            
            print("\nIDX: " + str(idx) + " SIZE: " + str(size) + "\n")
            DataAnalyseMethod([Header,Id,Velo,Road,PosX,PosY,STime, Timer, Slot])  # removido: DataAnalyseMethod(Cars) 
            idx+=1
            
except BaseException as e:
    IsRun=False # Finaliza a thread da análise de rede

    print("Erro: " + str(e))
    print("\nOperação Concluída: Gerando arquivos de Saída...\n")
    GenerateLogFilePorEstrada()
    # GenerateLogFilePorSlot() # suspenso para realizar o experimento com 70 carros (liberar dpeois)
    # PrintResumo() 

finally:
    IsRun=False
    print("\nA conexão atual foi encerrada.\n")   
