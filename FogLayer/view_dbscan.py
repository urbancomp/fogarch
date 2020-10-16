import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  matplotlib import style
import os

from array import *

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    print("Atualziando...\n")
    ax1.clear()  

    try:
        if (os.path.exists('dataview/data.csv')):
        
            data = pd.read_csv('dataview/data.csv')

            # _labels = pd.read_csv('dbscan/labels.csv')
            # labels = [i[0] for i in _labels.values.tolist()]

            X = StandardScaler().fit_transform(data)

            db = DBSCAN(eps=40, min_samples=3).fit(data)
            core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
            core_samples_mask[db.core_sample_indices_] = True
            labels = db.labels_

            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)

            print('Clusters: %d' % n_clusters_)
            print('Ruído: %d' % n_noise_)

            # core_samples_mask = np.zeros_like(labels, dtype=bool)
            # j=0 # insere true nas celulas sem ruído
            # for i in core_samples_mask:
            #     if (labels[j] != -1):
            #         core_samples_mask[j]=True
            #     j+=1

            unique_labels = set(labels)
            colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

            for k, col in zip(unique_labels, colors):
                if (k == -1):
                    # Black used for noise.
                    col = [0, 0, 0, 1]
                
                class_member_mask = (labels == k)

                #ax1.plot(X[:, 0], X[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
                #plt.scatter(X[:, 0], X[:, 1])
                # print("\nX\n")
                # print(X)
                # print("\nclass_member_mask\n")
                # print(class_member_mask)
                # print("\ncore_samples_mask\n")
                # print(core_samples_mask)
                # print("\nclass_member_mask & core_samples_mask\n")
                # print(class_member_mask & core_samples_mask)
                # print("\nclass_member_mask & ~core_samples_mask\n")
                # print(class_member_mask & ~core_samples_mask)


                xy = X[class_member_mask & core_samples_mask]
                plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
                
                xy = X[class_member_mask & ~core_samples_mask]
                plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)

                # ajusta titulo
                plt.title('DBSCAN: Number of Clusters: %d' % n_clusters_)
        
    except:
        print("Erro de Leitura...")

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


# def animate(i):
#     ax1.clear()  
#     #_X = pd.read_csv('dbscan/dbscan.csv')
#     data = pd.read_csv('dbscan/data.csv')
#     _labels = pd.read_csv('dbscan/labels.csv')

#     labels = [i[0] for i in _labels.values.tolist()]
#     X = StandardScaler().fit_transform(data)

#     core_samples_mask = np.zeros_like(labels, dtype=bool)
    
#     j=0 # insere true nas celulas sem ruído
#     for i in core_samples_mask:
#         if (labels[j] != -1):
#             core_samples_mask[j]=True
#         j+=1

#     unique_labels = set(labels)
#     colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

#     for k, col in zip(unique_labels, colors):
#         if k == -1:
#             # Black used for noise.
#             col = [0, 0, 0, 1]
        
#         class_member_mask = (labels == k)

#         #ax1.plot(X[:, 0], X[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
        
#         #plt.scatter(X[:, 0], X[:, 1])

#         xy = X[class_member_mask & core_samples_mask]
#         ax1.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=14)
        
#         xy = X[class_member_mask & ~core_samples_mask]
#         ax1.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col), markeredgecolor='k', markersize=6)
        
        
    
    
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()
    








    # lines = X.split('\n')
    # xs=[]
    # ys=[]
    # for line in lines:
    #     if len(line)>1:
    #         x,y = line.split(',')
    #         xs.append(x)
    #         ys.append(y)
    # ax1.clear()
    # #ax1.scatter(xs,ys)
    # ax1.scatter(xs,ys, cmap="plasma")

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()




# def animate(i):
#     graph_data = open('dbscan/dbscan.csv','r').read()
#     lines = graph_data.split('\n')
#     xs=[]
#     ys=[]
#     for line in lines:
#         if len(line)>1:
#             x,y = line.split(',')
#             xs.append(x)
#             ys.append(y)
#     ax1.clear()
#     ax1.scatter(xs,ys)

# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()