import pandas as pd
import numpy as np
import pprint
import time

from keras.models import load_model
from keras.utils import to_categorical

from data_importation import importation
from print_time import print_time

##################
### Load model ###
##################

print("Loading model...")
model = load_model('models/OK_128_model.h5')
# model.summary()

########################
### Data Importation ###
########################

path = 'data/data.txt'
X,y = importation(path)

#########################
### Prediction making ###
#########################

def rounded(pred):
    rounded = []
    for p in pred:
        p1 = round(p[0])
        p2 = round(p[1])
        rounded.append([p1,p2])
    pprint.pprint(rounded)

# One right and one wrong data
pred1 = np.array([[50,10,40,40,3,5,75,180,20,75,40,70],[500,10,40,40,3,5,75,180,20,75,40,70]])
# Wrong data
pred2 = np.array([[48.32444621571115,10.05710280759324,38.74348853203314,33.850704522228476,2.8824158014591745,5.034959848563274,78.016987932912,150.3849006842022,12.072886123155685,71.25795379650032,52.66637454005371,72.5001700066042],[50.026920841992165,9.518274096453377,39.73370980298786,34.888092123388724,3.135523884799747,4.781466079165229,72.2474564256202,114.26030588442762,23.25916978375616,81.91600633270413,49.22509257431758,68.08372549057498],[53.28451606589818,9.105876104980164,37.811811516457794,29.52419077643213,2.8541392579752585,6.1932632101099,80.35179852953753,169.3470443426398,13.541393734677232,74.68918489941203,41.632770578313696,75.08338055861897]])
# Right data
pred3 = np.array([[49.732107740505754,10.145839708309431,39.82462565224783,37.78098598693041,3.01202156050181,5.035940221948968,73.88145112956721,174.81822945773618,20.76545287163798,76.03890369566622,39.13723789955608,68.99068715487157],[50.55217382304805,9.85189679577659,39.80583672108063,33.554953455084714,3.060846316338611,4.945227772441047,75.27936185442152,178.76121455970195,22.12664119481611,73.87191484344595,37.74566371511486,69.47210540935805],[49.87639585433642,9.966764284719686,39.93812389883415,39.06329760878562,3.0356883228710627,5.101769408520894,74.86673475748394,189.06990855197742,19.47915193665339,74.81740868429961,38.800238000111925,70.93392016500042]])

start = time.time()
predictions1 = model.predict(pred1)
predictions2 = model.predict(pred2)
predictions3 = model.predict(pred3)
end = time.time()

rounded(predictions1)
rounded(predictions2)
rounded(predictions3)

print("New data:")
print_time(start,end)

# Calculate the time do to all the predictions
start = time.time()
predictions = model.predict(X)
end = time.time()

print("All data:")
print_time(start,end)