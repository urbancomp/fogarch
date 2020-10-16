

from __future__ import absolute_import
from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

import os
import sys

import matplotlib.colors as colors

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import sumolib  # noqa
from sumolib.visualization import helpers

# /usr/bin/python3 ..//plot_net_selection1.py -n colonia.net.xml -i selected_roads.txt --selected-width 1 --edge-width .5 -o selec ted_ez.png --edge-color '#606060' --selected-color '#7fffff'

# /usr/bin/python3 chart4.py -n colonia.net.xml -i selected_roads.txt --selected-width 1 --edge-width .5 -o selec ted_ez.png --edge-color '#606060' --selected-color '#7fffff'


def SetClasse(value):
    if isinstance(value, float):
        if (value >= 0 and value <= 0.15): return 1 #'Free-flow'
        elif (value > 0.16 and value <= 0.33): return 2 #'Reasonably Free-flow'
        elif (value > 0.33 and value <= 0.50): return 3 #'Stable-flow'
        elif (value > 0.50 and value <= 0.60): return 4 #'Approaching unstable-flow'
        elif (value > 0.60 and value <= 0.70): return 5 #'Unstable-flow'
        elif (value > 0.70 and value <= 1.00): return 6 #'Breakdown-flow'
        else:
             return 1 
    else:
        return str(value)


def main(args=None):
    """The main function; parses options and plots"""
    # ---------- build and read options ----------
    
    from optparse import OptionParser
    
    optParser = OptionParser()

    optParser.add_option("-n", "--net")
    # optParser.add_option("-i", "--selection", dest="selection", metavar="FILE", help="Defines the selection to read")
    optParser.add_option("--selected-width", dest="selectedWidth", type="float", default=1, help="Defines the width of selected edges")
    optParser.add_option("--color", "--selected-color", dest="selectedColor", default='#7fffff', help="Defines the color of selected edges")
    optParser.add_option("--edge-width", dest="defaultWidth", type="float", default=.2, help="Defines the width of not selected edges")
    optParser.add_option("--edge-color", dest="defaultColor", default='#606060', help="Defines the color of not selected edges")
    optParser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="If set, the script says what it's doing")
    
    
    # standard plot options
    helpers.addInteractionOptions(optParser)
    helpers.addPlotOptions(optParser)
    # parse
    options, remaining_args = optParser.parse_args(args=args)

    if options.net is None:
        print("Error: a network to load must be given.")
        return 1
    
    net = sumolib.net.readNet(options.net)

    fig, ax = helpers.openFigure(options)
    ax.set_aspect("equal", None, 'C')
    helpers.plotNet(net, "r", "2", options)
    options.nolegend = True
    
    ax.tick_params(labelsize='24', width=0)

    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    

    EXP = "70"

    # BASELINE GERAL ***************************************
    df1 = pd.read_csv("../../repositorio/" + EXP + "/Result_LOS_GERAL.csv")
    df1['Slot'] = df1['Slot'].astype(int)
    df1['Media']  =  df1['Media'].astype(float)
    df1['Velo']  =  df1['Velo'].astype(float)
    df1['Classe']  =  df1['Classe'].astype(float)
    df1['STime']  =  df1['STime'].astype(float)
    df1['Timer']  =  df1['Timer'].astype(float)
    df1['Source'] = 1

    # df5['ClusterLOS'] =  df5['ClusterLOS'].astype(float)
    df1['ClasseNum'] = df1['Classe'].map(lambda x: SetClasse(x))
    res = df1
    res.sort_values(by=['STime'])
    df1_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]


    # BASELINE 1TO2 ***************************************
    df2 = pd.read_csv("../../repositorio/" + EXP + "/Result_BASELINE_1TO2.csv")
    df2['Slot'] = df2['Slot'].astype(int)
    df2['Media']  =  df2['Media'].astype(float)
    df2['Velo']  =  df2['Velo'].astype(float)
    df2['Classe']  =  df2['Classe'].astype(float)
    df2['STime']  =  df2['STime'].astype(float)
    df2['Timer']  =  df2['Timer'].astype(float)
    df2['Source'] = "1TO2"

    df2['ClasseNum'] = df2['Classe'].map(lambda x: SetClasse(x))
    res = df2
    res.sort_values(by=['STime'])
    df2_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]

    # BASELINE RANDOM ***************************************
    df3 = pd.read_csv("../../repositorio/" + EXP + "/Result_BASELINE_RANDOM.csv")
    df3['Slot'] = df3['Slot'].astype(int)
    df3['Media']  =  df3['Media'].astype(float)
    df3['Velo']  =  df3['Velo'].astype(float)
    df3['Classe']  =  df3['Classe'].astype(float)
    df3['STime']  =  df3['STime'].astype(float)
    df3['Timer']  =  df3['Timer'].astype(float)
    df3['Source'] = "RAND"

    df3['ClasseNum'] = df3['Classe'].map(lambda x: SetClasse(x))
    res = df3
    res.sort_values(by=['STime'])
    df3_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]

    # BASELINE THRESHOLD ***************************************
    df4 = pd.read_csv("../../repositorio/" + EXP + "/Result_BASELINE_THRESHOLD.csv")
    df4['Slot'] = df4['Slot'].astype(int)
    df4['Media']  =  df4['Media'].astype(float)
    df4['Velo']  =  df4['Velo'].astype(float)
    df4['Classe']  =  df4['Classe'].astype(float)
    df4['STime']  =  df4['STime'].astype(float)
    df4['Timer']  =  df4['Timer'].astype(float)
    df4['Source'] = "LIM-5"

    df4['ClasseNum'] = df4['Classe'].map(lambda x: SetClasse(x))
    res = df4
    res.sort_values(by=['STime'])
    df4_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]


    # DBSCAN ***************************************
    df5 = pd.read_csv("../../repositorio/" + EXP + "/Result_LOS_DBSCAN.csv") 
    df5['Slot'] = df5['Slot'].astype(int)
    df5['Media']  =  df5['Media'].astype(float)
    df5['Classe']  =  df5['Classe'].astype(float)
    df5['STime']  =  df5['STime'].astype(float)
    df5['Timer']  =  df5['Timer'].astype(float)
    df5['Clusteres'] =  df5['Clusteres'].astype(int)
    df5['Source'] = 5
    
    # df5['ClusterLOS'] =  df5['ClusterLOS'].astype(float)
    df5['ClasseNum'] = df5['Classe'].map(lambda x: SetClasse(x))
    res = df5
    res.sort_values(by=['STime'])
    df5_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]
    # *****************************************************************************************

    # XMEANS ***************************************
    df6 = pd.read_csv("../../repositorio/" + EXP + "/Result_LOS_XMEANS.csv") 
    df6['Slot'] = df6['Slot'].astype(int)
    df6['Media']  =  df6['Media'].astype(float)
    df6['Media']  =  df6['Media'].astype(float)
    df6['LOS']  =  df6['Classe'].astype(float)
    df6['STime']  =  df6['STime'].astype(float)
    df6['Clusteres'] =  df6['Clusteres'].astype(int)
    df6['Source'] = 6
    

    df6['ClasseNum'] = df6['Classe'].map(lambda x: SetClasse(x))
    res = df6
    res.sort_values(by=['STime'])
    df6_select = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]
    # *****************************************************************************************

    res = pd.concat([df6_select], sort=False) # <<<<<<<<<<<<<<<<<<<<<<< MUDAR ANTES DE GERAR

    res = res[['RoadTag','Slot','Source','STime', 'Velo','PosX','PosY','ClasseNum','Descricao']]
    
    df1_velo = res[['Velo']]
    lista_velo = df1_velo.values.tolist()
    

    LOS = res[['ClasseNum','Descricao']].copy()
    LOS.drop_duplicates(subset=None, keep="first", inplace=True)
    LOS=LOS.sort_values(by=['ClasseNum'])
    print(LOS)
    
    color=['#54DB1D','#E9F010', '#F0B310','#f0af02','#d88888','#C30000']

    idx=0

    for index, row in LOS.iterrows():

        LOSFIlter = res.loc[(res['Descricao'] == row['Descricao'])]
        
        PosX = LOSFIlter[['PosX']]
        LPosX = PosX.values.tolist()

        df1_PosY = LOSFIlter[['PosY']]
        LPosY = df1_PosY.values.tolist()            

        plt.scatter(LPosX, LPosY, s=1.5, marker='o', c=color[idx], label=row['Descricao'])
        
        idx+=1

    ax.legend().set_visible(False)
    
    # plt.savefig('img/MAPA_BASELINE_30_' + EXP + '.eps', format='eps', dpi=200) 
    # plt.savefig('img/MAPA_BASELINE_30_' + EXP + '.png', format='png', dpi=200) 


    # df_los = res[['ClasseNum']]
    # Lista_los = df_los.values.tolist()

    # df1_PosX = res[['PosX']]
    # lista_PosX = df1_PosX.values.tolist()

    # df1_PosY = res[['PosY']]
    # lista_PosY = df1_PosY.values.tolist()    

    # x = lista_PosX
    # y = lista_PosY 

    # ax.add_artist(legend1)
    helpers.closeFigure(fig, ax, options)


if __name__ == "__main__":
    sys.exit(main(sys.argv))


    # comando 
    # /usr/bin/python3 chart4.py -n colonia.net.xml --selected-width 4 --edge-width 1 -o selected_ez.png --edge-color '#D6DBDF' --selected-color '#7fffff'
    #