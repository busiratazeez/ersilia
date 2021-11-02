import h5py
import numpy as np


class Hdf5Data(object):
    def __init__(self, values, keys, inputs, features):
        self.values = np.array(values, dtype=np.float32)
        self.keys = keys
        self.inputs = inputs
        self.features = features

    def save(self, filename):
        with h5py.File(filename, "w") as f:
            f.create_dataset("Values", data=self.values)
            f.create_dataset("Keys", data=self.keys)
            f.create_dataset("Inputs", data=self.inputs)
            f.create_dataset("Features", data=self.features)
