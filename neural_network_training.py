import pandas as pd
import numpy as np
import time
import pprint

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split

from data_importation import importation
from print_time import print_time

########################
### Data Importation ###
########################

path = 'data/data.txt'
X,y = importation(path)

##################
### Preprocess ###
##################

## 1 in y will be transformed in [0., 1.] and 0 in y will be transformed in [1., 0.]
y = to_categorical(y)
input_shape=X.shape[1]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.25)

######################
### Model creation ###
######################

print("Creating model...")
model = Sequential()

## Creating the "basis" model
model.add(Dense(64,activation='sigmoid',input_shape=(input_shape,)))
model.add(Dense(128,activation='sigmoid'))
model.add(Dense(128,activation='sigmoid'))
model.add(Dense(2, activation='softmax'))

## Creating the "fog" model
# model.add(Dense(128,activation='sigmoid',input_shape=(input_shape,)))
# model.add(Dense(64,activation='sigmoid'))
# model.add(Dense(6,activation='sigmoid'))
# model.add(Dense(6,activation='sigmoid'))
# model.add(Dense(6,activation='sigmoid'))
# model.add(Dense(2, activation='softmax'))

#model.summary()
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
early_stopping = EarlyStopping(patience = 5, restore_best_weights = True)

######################
### Model Training ###
######################

start = time.time()
model_training = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs=50, shuffle=False, callbacks=[early_stopping], batch_size=32)
end = time.time()

print_time(start,end)

####################
### Model Saving ###
####################

print("Saving model...")
model.save("models/model.h5")

########################
### Model evaluation ###
########################

print("Evaluating model...")
scores = model.evaluate(X, y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))