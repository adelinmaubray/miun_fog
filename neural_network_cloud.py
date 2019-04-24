import pandas as pd
import numpy as np
import time

from keras.models import load_model
from keras.models import Model
from keras import backend as K

from data_importation import importation
from print_time import print_time

##################
### Load model ###
##################

print("Loading model...")
model = load_model('models/OK_6_128_model.h5')
#model.summary()

############################
### Features Importation ###
############################

print("Importing features...")
features = pd.read_csv("output/output.txt", sep='\t')

##########################
### New model creation ###
##########################

start = time.time()
get_intermediate_output = K.function([model.layers[3].input], [model.layers[5].output])
layer_output = get_intermediate_output([features])[0]
end = time.time()

print_time(start,end)
print(layer_output.shape)