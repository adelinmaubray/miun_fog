import pandas as pd
import numpy as np
import time
import pprint

import tensorflow as tf
sess = tf.Session()

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping

from sklearn.model_selection import train_test_split

########################
### Data Importation ###
########################

# Import created data
print("Importing data...")
data = pd.read_csv('data/data.txt', sep='\t')
# Take the output
y = data['Running']
del data['Running']
X = data.values
y = y.values

##################
### Preprocess ###
##################

## 1 in y will be transformed in [0., 1.] and 0 in y will be transformed in [1., 0.]
y = to_categorical(y)
input_shape=X.shape[1]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.25)

start = time.time()
## Creating the model
print("Creating model...")
model = Sequential()
model.add(Dense(64,activation='sigmoid',input_shape=(input_shape,)))
model.add(Dense(128,activation='sigmoid'))
model.add(Dense(128,activation='sigmoid'))
#model.add(Dense(126,activation='relu'))
#model.add(Dense(126,activation='relu'))
model.add(Dense(2, activation='softmax'))
#model.summary()
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

early_stopping = EarlyStopping(patience = 5, restore_best_weights = True)

model_training = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs=50, shuffle=False, callbacks=[early_stopping], batch_size=32)
print("Saving model...")
model.save("models/model.h5")

end = time.time()
# print("Time : {} ".format(end - start))
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
# print("percentage of good prediction : {} %\n".format(model_training.history['val_acc'][0]*100))

# evaluate the model
print("Evaluating model...")
scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
pred = np.array([[50,10,40,40,3,5,75,180,20,75,40,70],[500,100,400,400,30,50,750,1800,200,750,400,700]])
predictions = model.predict(pred)
print(predictions)

rounded = []
for p in predictions:
    p1 = round(p[0])
    p2 = round(p[1])
    rounded.append([p1,p2])
pprint.pprint(rounded)

# predictions = model.predict(X)
# for p in predictions:
#     p1 = round(p[0])
#     p2 = round(p[1])
#     rounded.append([p1,p2])
#pprint.pprint(rounded)

# round predictions
# rounded = [round(x[0]) for x in predictions]
# print(rounded)

sess.close()