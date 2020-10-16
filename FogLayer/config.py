NETWORK = {
  "host": "", # Para o cliente o host deve ser vazio, a fim de denotar o recebimento a partir de qualquer ip origem
  "port": 4447,
  "host_destino": "localhost",
  "port_destino": 4448
}

GERAL = {
  "RoadFilter": [],   # [] ["28", "29"]
  "bytes_recebidos": 300,
  "lenght_via": 10000,
  "interval": 50,
  "Configuracao": 4
        # 1: Baseline geral com divisões por slot
        # 2: DBSCAN: Retorna amostra % de clusteres 
        # 3: DBSCAN: Retorna apenas os primeiros exemplares de cada cluster
        # 4: XMEANS: Retorna apenas os primeiros exemplares de cada cluster
        # 5: BASELINE:  1 to 2
        # 6: BASELINE:  Decide de forma aleatória os registros que serão gravados 
        # 7: BASELINE:  define que vei ser gravado a partir de um limite (threshold)

}

DBSCAN = {
  "raio_dbscan": 40,
  "min_amostra": 2
}

CONSTANTES = {
  # "RemotePathFiles": f"/home/edsonmottac/mnt/temp/",
  "RemotePathFiles": "data/",

}

Temp=[]
interval=0
CountCluster=0
