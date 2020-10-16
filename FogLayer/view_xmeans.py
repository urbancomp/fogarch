import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler


from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils import read_sample
from pyclustering.samples.definitions import SIMPLE_SAMPLES



import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  matplotlib import style
import os

from pyclustering.utils.color import color as color_list

from array import *

style.use('fivethirtyeight')


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
 


def animate(i):
    ax1.clear()  
    fig.clf()
    visualizer = cluster_visualizer()   
    
    print('Atualizando...')
    try:
        if (os.path.exists('dataview/data.csv')):
            
            data_select = pd.read_csv('dataview/data.csv')
            data = np.asarray(data_select).tolist()

            initial_centers = kmeans_plusplus_initializer(data, 2).initialize() # kmenas inicia com uam pesuqsia por 2 clusteres
            instances = xmeans(data, initial_centers, ccore=False) # aplica o xmeans executando os clusteres
            instances.process()

            clusters = instances.get_clusters()
            centers = instances.get_centers()
    
            
            # print("\n\DADOS")
            # print(data)
            
            # print("\n\nCLUSTERES")
            # print(clusters)
            
            # print("\n\nCENTROS")
            # print(centers)

            # print("\n\n\n")

            # i=0
            # distances = []
            # min_dist = 10000000000 
            # min_label=0
            # for c in clusters:
            #     # pega o primeiro centroide
            #     # print(c)
            #     print("\n\n*** loop centros****")
            #     print(centers[i])
            #     print("******************\n\n")

            #     for lbl in c:
            #         print("\n\n***Testando label***")
            #         print(lbl)
            #         print("*******************\n\n")
                    
            #         mean_distance = [np.sqrt((x-centers[i][0])**2+(y-centers[i][1])**2) for x, y in np.nditer(data[lbl])]
                    
            #         print("Teste Distância")
            #         print(mean_distance[0])
            #         if (min_dist>=mean_distance[0]):
            #             print("Essa é menor")
            #             min_dist = mean_distance[0]
            #             min_label = lbl

            #     i+=1 
            #     print("\n\nMENOR DISTÂNCIA")
            #     print(min_dist)

            #     print("\n\nROTULO DO MENOR")
            #     print(min_label)


            visualizer.append_clusters(clusters, data)
            visualizer.append_cluster(centers, None, marker='*', markersize=9, color='red') # 
            
            visualizer.show(fig, shift=0, display=True)
            
            plt.title('xMeans: Number of Clusters: %d' % len(clusters))
    except:
        print("Erro de Leitura...")
        
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False)
# visualizer.show()
plt.show()

