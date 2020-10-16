import csv
import time
import psutil
import os


send_method = 0 

# Obtém parâmetros de linha de comando 
import sys

if (len(sys.argv) > 1):
    send_method = sys.argv[1]
else:
    print("\n\nInforme o codigo do algoritmo a ser monitorado\n\n")
    sys.exit()


# send_method=7
RemotePathFiles = "/"

#rede
MEDIA_NET=0.0
COUNT_UPLOAD=0.0
COUNT_REGISTRO=0.0

ul=0
dl=0
t0 = time.time()
total_bytes=0.0

drive="enp0s17"

upload=psutil.net_io_counters(pernic=True)[drive][0]
download=psutil.net_io_counters(pernic=True)[drive][1] 
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
wtr.writerow (['Download','Upload', 'Tempo', 'Bytes'])
ul_previous=0.0
try:

    while True:
        
        last_up_down = up_down
        upload=psutil.net_io_counters(pernic=True)[drive][0]
        download=psutil.net_io_counters(pernic=True)[drive][1]
        t1 = time.time()
        up_down = (upload,download)

        total_bytes = total_bytes + ((upload - last_up_down[0])/1024)

        try:
            
            ul, dl = [(now - last) / (t1 - t0) / 1024.0 
                    for now,last in zip(up_down, last_up_down)]             
            t0 = time.time()

        except:
            pass

        if (dl>0.1 or ul>=0.1):
            time.sleep(2) 
            os.system('clear')
            print('UL: {:0.2f} kB/s \n'.format(ul)+'DL: {:0.2f} kB/s'.format(dl))
            
            
            wtr.writerow ([dl, ul,time.time(), total_bytes])

        
        COUNT_UPLOAD = COUNT_UPLOAD + ul
        COUNT_REGISTRO = COUNT_REGISTRO + 1
        
    v=input()

except:
    print("fim")




    