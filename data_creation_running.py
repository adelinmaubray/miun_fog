import numpy as np
import pandas as pd
from parameters import *

############################
### True Data Generation ###
############################

### Fermentation
def fermentation_creation():
    treacle = np.random.normal(t_treacle,t_treacle_tol/8,time)
    seeding = np.random.normal(t_seeding,t_seeding_tol/8,time)
    water = np.random.normal(t_water,t_water_tol/8,time)
    temperature = np.random.normal(T_1,T_1_tol/8,time)
    pression = np.random.normal(p,p_tol/8,time)
    pH_temp = np.random.normal(pH,pH_tol/8,time)
    out = np.random.normal(pourcentage_output_1,pourcentage_output_1_tol/8,time)

    df = pd.DataFrame({'Treacle' : treacle,
                        'Seeding' : seeding,
                        'Water' : water,
                        'Temperature' : temperature,
                        'Pression' : pression,
                        'pH' : pH_temp,
                        'Must' : out})

    running = []
    tmp = 1
    for index, row in df.iterrows():
        if tmp == 1:
            if not t_treacle - t_treacle_tol <= row['Treacle'] <= t_treacle + t_treacle_tol:
                tmp = 0
                print(index)
            elif not t_seeding - t_seeding_tol <= row['Seeding'] <= t_seeding + t_seeding_tol:
                tmp = 0
                print(index)
            elif not t_water - t_water_tol <= row['Water'] <= t_water + t_water_tol:
                tmp = 0
                print(index)
            elif not T_1 - T_1_tol <= row['Temperature'] <= T_1 + T_1_tol:
                tmp = 0
                print(index)
            elif not p - p_tol <= row['Pression'] <= p + p_tol:
                tmp = 0
                print(index)
            elif not pH - pH_tol <= row['pH'] <= pH + pH_tol:
                tmp = 0
                print(index)
            elif not pourcentage_output_1 - pourcentage_output_1_tol <= row['Must'] <= pourcentage_output_1 + pourcentage_output_1_tol:
                tmp = 0
                print(index)
        running.append(tmp)
            
    print(tmp)
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

def separator_creation():
    tour_minute = np.random.normal(tr_min,tr_min_tol/8,time)
    tempature = np.random.normal(T_2,T_2_tol/8,time)
    out = np.random.normal(t_output_2,t_output_2_tol/8,time)

    df = pd.DataFrame({'Rotation Speed' : tour_minute,
                        'Temperature' : tempature,
                        'Output' : out})

    running = []
    tmp = 1
    for index, row in df.iterrows():
        if tmp == 1:
            if not tr_min - tr_min_tol <= row['Rotation Speed'] <= tr_min + tr_min_tol:
                tmp = 0
                print(index)
            elif not T_2 - T_2_tol <= row['Temperature'] <= T_2 + T_2_tol:
                tmp = 0
                print(index)
            elif not t_output_2 - t_output_2_tol <= row['Output'] <= t_output_2 + t_output_2_tol:
                tmp = 0
                print(index)
        running.append(tmp)
            
    print(tmp)
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

def washer_creation():
    hum = np.random.normal(humidity,humidity_tol/8,time)
    out = np.random.normal(t_output_3,t_output_3_tol/8,time)

    df = pd.DataFrame({'Humidity' : hum,
                        'Output' : out})

    running = []
    tmp = 1
    for index, row in df.iterrows():
        if tmp == 1:
            if not humidity - humidity_tol <= row['Humidity'] <= humidity + humidity_tol:
                tmp = 0
                print(index)
            elif not t_output_3 - t_output_3_tol <= row['Output'] <= t_output_3 + t_output_3_tol:
                tmp = 0
                print(index)
        running.append(tmp)
            
    print(tmp)
    df['Running'] = running
    print(df['Running'].value_counts())
    return df

# i = 34
# fermentation_creation().to_csv('data/fermentation' + str(i) + '.txt', header = None, index = None, sep='\t')
# separator_creation().to_csv('data/separator' + str(i) + '.txt', header = None, index = None, sep='\t')
# washer_creation().to_csv('data/washer' + str(i) + '.txt', header = None, index = None, sep='\t')
for i in range(1,61):
    # pass
    print(i)
    fermentation_creation().to_csv('data/fermentation' + str(i) + '.txt', header = None, index = None, sep='\t')
    separator_creation().to_csv('data/separator' + str(i) + '.txt', header = None, index = None, sep='\t')
    washer_creation().to_csv('data/washer' + str(i) + '.txt', header = None, index = None, sep='\t')