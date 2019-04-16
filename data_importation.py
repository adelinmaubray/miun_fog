import pandas as pd
from parameters import *

########################
### Data Importation ###
########################

# Import from different txt file
def import_split():
    data = pd.DataFrame()

    for i in range(1,61):
        print(i)

        ### Right data
        data1 = pd.read_csv('data/fermentation' + str(i) + '.txt', header = None, sep='\t')
        data1.columns = ['Treacle input','Seeding input','Water input','Temperature 1','Pression','pH','Must', 'Running 1']

        data2 = pd.read_csv('data/separator' + str(i) + '.txt', header = None, sep='\t')
        data2.columns = ['Rotation Speed','Temperature 2','Yeast', 'Running 2']

        data3 = pd.read_csv('data/washer' + str(i) + '.txt', header = None, sep='\t')
        data3.columns = ['Humidity','Washed Yeast', 'Running 3']

        df1 = data1.join(data2).join(data3)

        ### Wrong data
        data1 = pd.read_csv('data/fermentation_wrong' + str(i) + '.txt', header = None, sep='\t')
        data1.columns = ['Treacle input','Seeding input','Water input','Temperature 1','Pression','pH','Must', 'Running 1']

        data2 = pd.read_csv('data/separator_wrong' + str(i) + '.txt', header = None, sep='\t')
        data2.columns = ['Rotation Speed','Temperature 2','Yeast', 'Running 2']

        data3 = pd.read_csv('data/washer_wrong' + str(i) + '.txt', header = None, sep='\t')
        data3.columns = ['Humidity','Washed Yeast', 'Running 3']

        df2 = data1.join(data2).join(data3)

        df = pd.concat([df1,df2])

        running = []
        for index, row in df.iterrows():
            tmp = 1
            if row['Running 1'] == 0:
                tmp = 0
            elif row['Running 2'] == 0:
                tmp = 0
            elif row['Running 3'] == 0:
                tmp = 0
            running.append(tmp)

        df['Running'] = running
        del df['Running 1']
        del df['Running 2']
        del df['Running 3']

        data = pd.concat([data,df])

    print('Saving')
    data.to_csv('data/data.txt', sep='\t', index=False)
    print(data['Running'].value_counts())
    return data

def import_one():
    print('Importing')
    #names = ['Treacle input','Seeding input','Water input','Temperature 1','Pression','pH','Must', 'Rotation Speed','Temperature 2','Yeast', 'Humidity','Washed Yeast', 'Running']
    data = pd.read_csv('data/data.txt', sep='\t')
    return data


data = import_split()
# data = import_one()
print(data)