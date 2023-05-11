import numpy as np
from animate import Animate
from observables import Observables
from algorithms import Algorithms

class Simulate(object):

    def __init__(self, l, p):

        self.observables= Observables()
        self.l= l
        self.p= p
        self.N= self.l**2
        self.algorithms= Algorithms(self.l, self.p)

    def gneerateInitialLattice(self):

        self.arr= np.random.choice(np.array([0, 1]), size=(self.l, self.l))

    def runSimulationVisualisation(self):
        
        self.epoch=0
        self.sweeps=0
        self.gneerateInitialLattice()
        self.animation= Animate(self.arr)

        while True:
            self.arr= self.algorithms.updateLattice(self.arr)
            self.epoch += 1
            
            if self.epoch % self.N ==0:
                self.sweeps+=1
                print(self.sweeps)
                self.animation.drawImage(self.arr)

if __name__ == '__main__':
    
    # Visualisation
    simulation= Simulate(50, 0.6)
    simulation.runSimulationVisualisation()
