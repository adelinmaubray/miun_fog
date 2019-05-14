# miun_fog

## Running Deep Learning algorithms in a Fog Computing architecture to predict maintenance in an IIoT scenario

The goal of this Master's Thesis was to survey if it is feasible, useful and effective to use Deep Learning algorithms in a Fog Computing architecture.  The scenario was to predictive maintenance in an industrial context (```industrial/yeast_production.PNG``` image).  Here is the code explanation.

### Data creation

Before running Deep Learning algorithms, it is necessary to create data.  The input data have 12-dimension size.  The output is 0 (not_running data) or 1 (running data).  Sensors make measurements every 10 seconds during 60 days.  6 (min) x 60 (h) x 24 (j) x 60 = 518.400 measurements.

* ```print_time.py``` is just a function which print the time difference between to moments
* ```parameters.py``` provides all the parameters for the chosen industrial scenario.  There are the normal variables and the tolerances
* ```data_creation_running.py``` allows to create the "running data" (output = 1).  It creates 1 file per day per machine ```data/machineXX.txt```
* ```data_creation_not_running.py``` allows to create the "not_running data" (output = 0) according several conditions.  It creates 1 file per day per machine ```data/machine_wrongXX.txt```
* ```data_creation_merge.py``` allows to merge all the created files in only one file ```data/data.txt```.  This file is too large for GitHub, so ```data/data_test.txt``` is here as an example
* ```data_creation_importation.py``` allows to import the data file in a Python Pandas.DataFrame

### Training and testing: comparison

The first investigation was to train and test the deep neural network on a Fog node and compare the performances with a standard computer.  The exact same code ran on the devices:

* ```neural_network_training.py``` creates and trains the model using Keras and TensorFlow as backend - training time is measured.  The model is saved in ```models/``` folder.  ```models/128_model.h5``` is the resulting model.
* ```neural_network_testing.py``` tests the model on new data.  Testing time is measured and performance with new data.

### Testing in a Fog architecture

The last step is to deploy a little Fog architecture (one node) for the testing phase.  The lower layer are processed in the Fog node and the higher in the Cloud.  ```models/fog_6_128_model.h5``` is the model used for this part.

* ```neural_network_fog.py``` takes the input data and generates the intermediate features (by using a Keras function) which are saved in the ```output/```.  ```output/fog_6_128_output.txt``` are the intermediate generated features.
* ```neural_network_cloud.py``` takes the created features and process the higher layers.
* ```neural_network_comparison.py``` is just here to compare the performances of doing the all testing phase in the Cloud by using the same Keras function

### Comparison with other Machine Learning algorithms

It is legitimate to wonder if there are no better algorithms, that's why other Machine Learning algorithms have been implemented to make a comparison of the performance.

* ```comparison_knn.py``` implements the K-Nearest Neighbor algorithm
* ```comparison_perceptron.py``` implements the Perceptron algorithm
* ```comparison_svm.py``` implements the Support Vector Machine algorithm
* ```comparison_tree.py``` implements the Decision Tree algorithm