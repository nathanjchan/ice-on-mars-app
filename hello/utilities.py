import pickle
import numpy as np


def save_object(self, obj, file_name):
    """Given an object and a file name, save the item to local memory using pickle"""
    with open(file_name, "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    return


def load_object(self, file_name):
    """Given a file name, load an item from local memory using pickle, and return the object"""
    with open(file_name, "rb") as input:
        obj = pickle.load(input)
    return obj


def distance(x1, y1, x2, y2):
    return np.sqrt(np.sum((x1-x2)**2 + (y1-y2)**2))