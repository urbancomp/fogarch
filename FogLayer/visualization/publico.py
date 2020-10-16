
from dateutil import parser


def MediaPorIntervalor(res_select, interval_time=0.2):
        
    res_select = res_select[res_select['RoadTag']!=0]
    res_select.drop_duplicates(subset=None, keep="first", inplace=True)

    # cria campos
    res_select['Timer2']  =  0
    res_select['Media2']  =  0.0    

    velo_total = 0.0
    count=0 
    timer_atual = 0.0
    timer_ant = 0.0
    elapset_atual= 0.0
    elapset_cumulativo = 0.0

    count_timer=interval_time

    for index, row in res_select.iterrows():
        
        timer_atual  = row['STime']

        if (timer_ant!=0.0): 
            elapset_atual = float(row['STime']) - float(timer_ant)
            
            # print(abs(elapset_atual))
            
            elapset_cumulativo+=float(elapset_atual)
            
            if ((elapset_cumulativo >= interval_time)): 
                # print('Chegou')
                # break
                media_velo = velo_total / count
                res_select.at[index,"Media2"] = media_velo 
                res_select.at[index,"Timer2"] = count_timer
                
                elapset_cumulativo=0.0
                timer_ant = 0.0
                velo_total=0.0
                media_velo=0.0
                count=0

                count_timer+=interval_time

        if (timer_atual != timer_ant):
            timer_ant = timer_atual

        velo_total = velo_total + row['Velo']
        count+=1
    
    
    # remove zeros
    # res_select = res_select[res_select['Timer2']!=0]
    return res_select


def Filter(DATA, ROAD=0, SLOT=0):
    
    if ((ROAD!=0) & (SLOT!=0)):
        return DATA[(DATA['RoadTag']==ROAD) & (DATA['Slot']==SLOT)]
    elif ((ROAD!=0) & (SLOT==0)):
        return DATA[(DATA['RoadTag']==int(ROAD))]
    else:
        return DATA
    
