import numpy as np
from animate import Animate
from observables import Observables
from algorithms import Algorithms

class Simulation(object):

    def __init__(self):

        self.algorithms= Algorithms()
        self.observables= Observables()
