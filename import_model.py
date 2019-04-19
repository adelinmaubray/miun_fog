import pandas as pd
from keras.models import load_model
from keras.utils import to_categorical

# Load model
print("Load model...")
model = load_model('models/EasyData/Total/model_3_128_sigmoid_total.h5')

# Import created data
print("Importing data...")
data = pd.read_csv('data/EasyData/data.txt', sep='\t')
# Take the output
y = data['Running']
del data['Running']
X = data.values
y = to_categorical(y.values)

# Evaluating model
print("Evaluating model...")
scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))