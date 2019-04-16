import numpy as np
from keras.utils import to_categorical
from keras import models
from keras import layers
from keras.datasets import imdb


(training_data, training_targets), (testing_data, testing_targets) = imdb.load_data(num_words=10000)
data = np.concatenate((training_data, testing_data), axis=0)
targets = np.concatenate((training_targets, testing_targets), axis=0)
def vectorize(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results


data = vectorize(data)
print(data.shape)
print(data)
targets = np.array(targets).astype("float32")
test_x = data[:10000]
test_y = targets[:10000]
train_x = data[10000:]
train_y = targets[10000:]


model = models.Sequential()
# Input - Layer
model.add(layers.Dense(50, activation = "sigmoid", input_shape=(10000, )))
# Hidden - Layers
model.add(layers.Dense(50, activation = "sigmoid"))
model.add(layers.Dense(50, activation = "sigmoid"))
# Output- Layer
model.add(layers.Dense(1, activation = "sigmoid"))
# model.summary()


# compiling the model
model.compile(
 optimizer = "adam",
 loss = "binary_crossentropy",
 metrics = ["accuracy"]
)
results = model.fit(
 train_x, train_y,
 epochs= 2,
 batch_size = 500,
 validation_data = (test_x, test_y)
)
print("Test-Accuracy:", np.mean(results.history["val_acc"]))

predictions = model.predict(test_x)
print(predictions)