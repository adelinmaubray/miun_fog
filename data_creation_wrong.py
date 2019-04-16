import numpy as np
import pandas as pd
from parameters import *

#############################
### Wrong Data Generation ###
#############################

def fermentation_creation_wrong():
    input_1 = 100
    input_1_tol = input_1*tol/2

    treacle = np.random.normal(t_treacle*10,t_treacle_tol/1.0,time)
    seeding = np.random.normal(t_seeding*10,t_seeding_tol/1.0,time)
    water = np.random.normal(t_water*10,t_water_tol/1.0,time)
    temperature = np.random.normal(T_1*10,T_1_tol/1.0,time)
    pression = np.random.normal(p*10,p_tol/1.0,time)
    pH_temp = np.random.normal(pH*10,pH_tol/1.0,time)
    out = np.random.normal(pourcentage_output_1*10,pourcentage_output_1_tol/1.0,time)

    df = pd.DataFrame({'Treacle' : treacle,
                        'Seeding' : seeding,
                        'Water' : water,
                        'Temperature' : temperature,
                        'Pression' : pression,
                        'pH' : pH_temp,
                        'Must' : out})

    running = []    
    for index, row in df.iterrows():
        tmp = 1
        input = row['Treacle'] + row['Seeding'] + row['Water']
        if not t_treacle - t_treacle_tol <= row['Treacle'] <= t_treacle + t_treacle_tol:
            tmp = 0
        elif not t_seeding - t_seeding_tol <= row['Seeding'] <= t_seeding + t_seeding_tol:
            tmp = 0
        elif not t_water - t_water_tol <= row['Water'] <= t_water + t_water_tol:
            tmp = 0

        elif not input_1 - input_1_tol <= input <= input_1 + input_1_tol:
            tmp = 0
        
        elif not T_1 - T_1_tol <= row['Temperature'] <= T_1 + T_1_tol:
            tmp = 0
        elif not p - p_tol <= row['Pression'] <= p + p_tol:
            tmp = 0
        elif not pH - pH_tol <= row['pH'] <= pH + pH_tol:
            tmp = 0

        elif not T_1 - T_1_tol/2 <= row['Temperature'] <= T_1 + T_1_tol/2 and not p - p_tol <= row['Pression'] <= p + p_tol:
            tmp = 0
        elif not T_1 - T_1_tol/2 <= row['Temperature'] <= T_1 + T_1_tol/2 and not pH - pH_tol <= row['pH'] <= pH + pH_tol:
            tmp = 0
        
        elif not pourcentage_output_1 - pourcentage_output_1_tol/2 <= row['Must'] <= pourcentage_output_1 + pourcentage_output_1_tol/2:
            tmp = 0
        
        running.append(tmp)
            
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

def separator_creation_wrong():
    tour_minute = np.random.normal(tr_min*10,tr_min_tol*1.5,time)
    tempature = np.random.normal(T_2*10,T_2_tol*1.5,time)
    out = np.random.normal(t_output_2*10,t_output_2_tol*1.5,time)

    df = pd.DataFrame({'Rotation Speed' : tour_minute,
                        'Temperature' : tempature,
                        'Output' : out})

    running = []
    for index, row in df.iterrows():
        tmp = 1
        if not tr_min - tr_min_tol <= row['Rotation Speed'] <= tr_min + tr_min_tol:
            tmp = 0
        elif not T_2 - T_2_tol <= row['Temperature'] <= T_2 + T_2_tol:
            tmp = 0
        elif not t_output_2 - t_output_2_tol <= row['Output'] <= t_output_2 + t_output_2_tol:
            tmp = 0
        
        elif not tr_min - tr_min_tol/5 <= row['Rotation Speed'] <= tr_min + tr_min_tol/5 and not t_output_2 - t_output_2_tol/3 <= row['Output'] <= t_output_2 + t_output_2_tol/3:
            tmp = 0
        elif not T_2 - T_2_tol/5 <= row['Temperature'] <= T_2 + T_2_tol/5 and not t_output_2 - t_output_2_tol/5 <= row['Output'] <= t_output_2 + t_output_2_tol/5:
            tmp = 0
        elif not T_2 - T_2_tol/3 <= row['Temperature'] <= T_2 + T_2_tol/3 and not tr_min - tr_min_tol/3 <= row['Rotation Speed'] <= tr_min + tr_min_tol/3 and not t_output_2 - t_output_2_tol/3 <= row['Output'] <= t_output_2 + t_output_2_tol/3:
            tmp = 0
        
        running.append(tmp)
            
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

def washer_creation_wrong():
    hum = np.random.normal(humidity*10,humidity_tol,time)
    out = np.random.normal(t_output_3*10,t_output_3_tol,time)

    df = pd.DataFrame({'Humidity' : hum,
                        'Output' : out})

    running = []
    for index, row in df.iterrows():
        tmp = 1
        if not humidity - humidity_tol <= row['Humidity'] <= humidity + humidity_tol:
            tmp = 0
        elif not t_output_3 - t_output_3_tol <= row['Output'] <= t_output_3 + t_output_3_tol:
            tmp = 0

        elif not humidity - humidity_tol/5 <= row['Humidity'] <= humidity + humidity_tol/5 and not t_output_3 - t_output_3_tol/7 <= row['Output'] <= t_output_3 + t_output_3_tol/7:
            tmp = 0

        running.append(tmp)
            
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

# i = 60
# fermentation_creation_wrong().to_csv('data/fermentation_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')
# separator_creation_wrong().to_csv('data/separator_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')
# washer_creation_wrong().to_csv('data/washer_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')
for i in range(1,61):
    print(i)
    fermentation_creation_wrong().to_csv('data/fermentation_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')
    separator_creation_wrong().to_csv('data/separator_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')
    washer_creation_wrong().to_csv('data/washer_wrong' + str(i) + '.txt', header = None, index = None, sep='\t')