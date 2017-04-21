from sklearn.ensemble import RandomForestClassifier
import numpy as np

def load_from_sparsed(name, samples = 800, attributes = 100000):
    matrix = -1*np.ones((samples, attributes))
    with open(name, "r") as f:
        for (i, line) in enumerate(f):
            temp = f.readline()
            temp = temp.split(" ")
            index = [int(value)-1 for value in temp[:-1]]
            matrix[i, index] = 1
    return matrix

training = load_from_sparsed("dorothea_train.data")
classified = np.genfromtxt("dorothea_train.labels")

rfc = RandomForestClassifier(n_estimators=attributes, n_jobs = -1)

rfc.fit(training, classified)


"""
    Saves forest
"""
import pickle

with open('forest.pkl', 'wb') as f:
    pickle.dump(rf, f)
