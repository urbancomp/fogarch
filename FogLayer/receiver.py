from __future__ import with_statement

import socket
import threading
import time
import config
import timeit
import csv

DataReciver = []

def ReceiveSocketData():
    global DataReciver 
    
    # wtr = csv.writer(open ("data/teste.csv", 'a'), delimiter=',', lineterminator='\n')
    # wtr.writerow(['item1','item2'])

    # TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configurações
    server_address = (config.NETWORK["host"], config.NETWORK["port"])
    print('Starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    lock = threading.Lock()
    count=0
    while True:
        
        connection, client_address = sock.accept()
        data=''
           
        while True: 

            data = connection.recv(500)
            
            if data: 
                
                # divide os dados da recebidos via querystring por meio do delimitador ";"

                rows = data.decode("utf-8").split("\n")
                datafields = rows[0]
                row = datafields.split(";")
                # print(row)
                
                if (len(row) == 10):
                    with lock:
                        DataReciver.append(row)
                else:
                    count+=1
                    # print(row)
                    # print("ErrorRate: " + str(count))

