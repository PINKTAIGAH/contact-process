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

    def generateInitialLattice(self):

        self.arr= np.random.choice(np.array([0, 1]), size=(self.l, self.l))

    def recordActiveFractions(self):

        self.timeArray.append(self.sweeps)
        self.activeFractionArray.append(self.activeFraction)

    def findActiveFraction(self):
        self.activeFraction= np.count_nonzero(self.arr==1)/self.arr.size

    def findActiveNumber(self):
        self.activeFraction= np.count_nonzero(self.arr==1)

    def findActiveFractionStatistics(self):
        mean= np.array(self.activeFractionArray).mean()/self.N
        variance= np.array(self.activeFractionArray).var()/self.N
        return mean, variance
    
    def generate_resampled_var(self, data, n=1000):
    # Generate a resampled data set for Infection fraction and return it's variance
        resampled_dataset= np.random.choice(data, size=n)
        var= resampled_dataset.var()/self.N
        return var
    
    def find_resampled_variance(self, data, k=1000):
    # Return the errors from the resampled datasets
        variance_errors= []
        #Iterate over all p1 probabilities
        for i in range(data.shape[0]):
            bootstrapped_var= []
            for j in range(k):
                bootstrapped_var.append(self.generate_resampled_var(data[i][:]))
            variance_errors.append(np.array(bootstrapped_var).std())    
        return variance_errors
    
    def runSimulationVisualisation(self):
        
        self.epoch=0
        self.sweeps=0
        self.generateInitialLattice()
        self.animation= Animate(self.arr)

        while True:
            self.arr= self.algorithms.updateLattice(self.arr)
            self.epoch += 1
            
            if self.epoch % self.N ==0:
                self.sweeps+=1
                print(self.sweeps)
                self.animation.drawImage(self.arr)

    def runSimulationFractionPerTime(self, end=150):

        self.epoch=0
        self.sweeps=0
        self.finalTime= end
        self.timeArray=[]
        self.activeFractionArray= []
        self.generateInitialLattice()
        while True:
            self.arr= self.algorithms.updateLattice(self.arr)
            self.epoch += 1
            
            if self.epoch % self.N ==0:
                self.sweeps+=1
                print(self.sweeps)
                self.findActiveFraction()
                self.recordActiveFractions()

            if self.sweeps == 150:
                break

        np.savetxt(f'../Data/active_fraction_{self.p}.txt', np.array([self.timeArray, self.activeFractionArray]).T)

    def runSimulationAverageFraction(self, end=150):

        self.epoch=0
        self.sweeps=0
        self.finalTime= end
        self.activeFractionData= []
        self.probabilities= np.arange(0.55, 0.705, 0.005)
        self.generateInitialLattice()
        
        for i in range(self.probabilities.size):
            print(f'{i}/{self.probabilities.size} dp collected')
            self.p= self.probabilities[i]
            self.timeArray=[]
            self.activeFractionArray= []
            self.sweeps= 0

            while True:

                self.arr= self.algorithms.updateLattice(self.arr)
                self.epoch += 1
                
                if self.epoch % self.N ==0:
                    self.sweeps+=1
                    self.findActiveNumber()
                    self.recordActiveFractions()

                if self.sweeps == self.finalTime:
                    break
            self.activeFractionData.append(self.activeFractionArray)
        np.savetxt(f'../Data/active_fraction_average.txt', np.array(self.activeFractionData).T)

if __name__ == '__main__':
    
    # Visualisation
    # simulation= Simulate(50, 0.6)
    # simulation.runSimulationVisualisation()

    # part b
    # simulation= Simulate(50, 0.7)
    # simulation.runSimulationFractionPerTime()  

    # part c
    simulation= Simulate(50, 0.7)
    simulation.runSimulationAverageFraction()

