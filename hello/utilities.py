import numpy as np


def distance(x1, y1, x2, y2):
    return np.sqrt(np.sum((x1-x2)**2 + (y1-y2)**2))