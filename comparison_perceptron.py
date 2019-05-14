from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np
import time
import pprint

from data_importation import importation
from print_time import print_time

########################
### Data Importation ###
########################

path = 'data/data.txt'
X,y = importation(path)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.25, random_state = 4)

######################
### Model Training ###
######################

print("Training...")
percep = Perceptron()
start = time.time()
percep.fit(X_train, y_train)
end = time.time()
print("Training time:")
print_time(start,end)

#####################
### Model Testing ###
#####################

print("Testing...")
start = time.time()
y_pred = percep.predict(X_test)
end = time.time()
print("Testing time:")
print_time(start,end)

################
### Accuracy ###
################

score = accuracy_score(y_test, y_pred)
print("Accuracy score:")
print(score)