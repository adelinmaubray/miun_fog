import pandas as pd

def importation(path):
    # Import created data
    print("Importing data...")
    data = pd.read_csv(path, sep='\t')
    # Take the output
    y = data['Running']
    del data['Running']
    X = data.values
    y = y.values
    return [X,y]