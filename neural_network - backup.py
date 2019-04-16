import time
start = time.time()
import pandas as pd
import numpy as np
np.random.seed(176)
import matplotlib.pyplot as plt

import tensorflow as tf
sess = tf.Session()

from keras import backend as K
K.set_session(sess)

from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical


early_stopping_monitor = EarlyStopping(patience=6)

## importing the data
#X = pd.read_excel('./Datas/ATP_All_magouille.xlsx').values
#y = pd.read_excel('./Datas/ATP_Victories_magouille.xlsx').values
X = pd.read_excel('./Datas/ATP_All.xlsx').values
y = pd.read_excel('./Datas/ATP_Victories.xlsx').values
#X=X[-2000:]
#y=y[-2000:]
## 1 in y will be transformed in 0. 1. and 0 in y will be transformed in 1. 0.
y = to_categorical(y)
input_shape=X.shape[1]
## slpiting the data in 2 sets (train and test)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.3, random_state=176)
#X_test=X
#y_test=y
## creating the model
model = Sequential()
model.add(Dense(20,activation='linear',input_shape=(input_shape,)))
model.add(Dense(50,activation='linear'))
model.add(Dense(90,activation='linear'))
model.add(Dense(50,activation='linear'))
model.add(Dense(20,activation='linear'))
model.add(Dense(10,activation='linear'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
## fitting the model to the training data
#model_training = model.fit(X_train, y_train,epochs=40, batch_size=25, validation_data=(X_test, y_test),shuffle=False)#callbacks=[early_stopping_monitor],
model_training = model.fit(X, y,epochs=50, validation_data=(X_test, y_test),shuffle=False,callbacks=[early_stopping_monitor])#,batch_size=10)
end = time.time()
print("percentage of good prediction : {} %".format(model_training.history['val_acc'][-1]*100))
## ploting the evolution of the loss function over the epochs
#plt.plot(model_training.history['val_loss'], 'r')
#plt.xlabel('Epochs')
#plt.ylabel('Validation score')
#plt.show()
model.save("TEST.h5")
#model = load_model('20_90_20_10_linearModif.h5')
X_test=X[-750:]
y_test=y[-750:]
y_predict=model.predict(X_test)
<<<<<<< HEAD
it=0
nErr=0
v0=0
v1=0
for i in y_test:
    if i[0] != round(y_predict[it][0]) or i[1] != round(y_predict[it][1]) :
        v0+=y_predict[it][0]
        v1+=y_predict[it][1]
        nErr+=1
    it+=1
    
v0=v0/nErr
v1=v1/nErr
print("percentage of good prediction : "+str((1-nErr/it)*100)+" %")
<<<<<<< HEAD
print("moyenne des prédictions : {} , {}".format(v0,v1))
=======
=======

>>>>>>> 4bbd42068e9fb1962f13aeb191bed563d2a6ef9c
it=0
gain=0
mise=0
nVict=0
nDef=0
mises=[]

for i in y_test:
	if X_test[it][11]==0 and int(X_test[it][12])==0:
		pass
	tmp=abs(y_predict[it][0]-y_predict[it][1])
	if tmp<0.1:
		mises.append(0)
	elif tmp<0.2:
		mises.append(0.5)
	elif tmp<0.3:
		mises.append(1)
	elif tmp<0.4:
		mises.append(4)
	elif tmp<0.5:
		mises.append(8)
	elif tmp<0.6:
		mises.append(10)	
	elif tmp<0.7:
		mises.append(12)
	elif tmp<0.8:
		mises.append(15)
	else:
		mises.append(20)
	it+=1
print(sum(mises)/len(mises))
it=0
it2=-1
for i in y_test:
	if X_test[it][11]==0 and int(X_test[it][12])==0:
		pass
	elif y_predict[it][0]<=y_predict[it][1] and i[0]>=i[1]:
		it2+=1
		nDef+=1
		mise+=mises[it2]
		gain-=mises[it2]
	elif y_predict[it][0]>=y_predict[it][1] and i[0]<=i[1]:
		it2+=1
		nDef+=1
		mise+=mises[it2]
		gain-=mises[it2]		
	else:
		it2+=1
		if y_predict[it][0]<y_predict[it][1]:
			nVict+=1
			mise+=mises[it2]
			gain+=(X_test[it][11]-1)*mises[it2]
		elif y_predict[it][1]<=y_predict[it][0]:
			nVict+=1
			mise+=mises[it2]
			gain+=(X_test[it][12]-1)*mises[it2]
	it+=1
print("gain total : {} %".format(gain/mise*100))
<<<<<<< HEAD
print("nombre de victoire : {} \nnombre de défaites : {}".format(nVict,nDef))
>>>>>>> cc11c7d55a2310f803bc6b0627bdcd2e7b4ee337
=======
#print("nombre de victoire : {} \nnombre de défaites : {}".format(nVict,nDef))
print ("temps écoulé : {}".format(end - start))
>>>>>>> 4bbd42068e9fb1962f13aeb191bed563d2a6ef9c
