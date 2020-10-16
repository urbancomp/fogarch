import config
import csv
import time
import psutil
import os

# from analyse import *
import analyse as ann

# define o método de redução
send_method = config.GERAL["Configuracao"]  
RemotePathFiles = config.CONSTANTES["RemotePathFiles"]

#rede
MEDIA_NET=0.0
COUNT_UPLOAD=0.0
COUNT_REGISTRO=0.0

ann.ClearFolder("net/")

def PrintResumo():

    if (COUNT_REGISTRO >0): MEDIA_NET = COUNT_UPLOAD / COUNT_REGISTRO 

    print(chr(27) + "[2J")
    print("\n\n\n\n")
    print("***** RESUMO *****")
    print("\n\n")
    print("Media total de uplaod : " + str(MEDIA_NET))
    print("Tamanho final do arquivo enviado : " + str(os.path.getsize(RemotePathFiles + 'DBSCAN_All.csv')))
    print("\n\n")

count=0
qry=''

ul=0
dl=0
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
wtr.writerow (['Download','Upload', 'Tempo'])
ul_previous=0.0
try:

    while True:
        
        last_up_down = up_down
        upload=psutil.net_io_counters(pernic=True)['wlp3s0'][0]
        download=psutil.net_io_counters(pernic=True)['wlp3s0'][1]
        t1 = time.time()
        up_down = (upload,download)

        try:
            
            ul, dl = [(now - last) / (t1 - t0) / 1024.0 
                    for now,last in zip(up_down, last_up_down)]             
            t0 = time.time()

        except:
            pass

        if (dl>0.1 or ul>=0.1):
            time.sleep(2) 
            os.system('clear')
            #print('UL: {:0.2f} kB/s \n'.format(ul)+'DL: {:0.2f} kB/s'.format(dl))
            print('UL: {:0.2f} kB/s \n'.format(ul))
            wtr.writerow ([dl, ul,time.time()])

        
        COUNT_UPLOAD = COUNT_UPLOAD + ul
        COUNT_REGISTRO = COUNT_REGISTRO + 1
        
    v=input()

except:
    PrintResumo()




    