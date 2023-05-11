import numpy as np

class Observables(object):

    def findActiveFraction(arr):
        return np.count_nonzero(arr==1)/arr.size