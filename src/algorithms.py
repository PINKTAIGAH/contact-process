import numpy as np

class Algorithms(object):

    # In lattice we let : I ==> 0 and A ==> 1
    def __init__(self, l, p):

        self.l= l
        self.p= p
        self.upIndex= np.roll(np.indices((self.L, self.L)), -1, axis=0)
        self.downIndex= np.roll(np.indices((self.L, self.L)), +1, axis=0)
        self.rightIndex= np.roll(np.indices((self.L, self.L)), +1, axis=1)
        self.leftIndex= np.roll(np.indices((self.L, self.L)), -1, axis=1)

    def generateRandomIndex(self):

        self.i= tuple(np.random.randint(low= 0, high= self.l, size=(self.l, self.l)))
    
    def chooseRandomNeighbour(self):
        # Pick random index for nearest neighbour
        # 0 ==> up
        # 1 ==> down
        # 2 ==> right
        # 3 ==> left
        self.randomNeighbourListIndex= np.random.choice([0,1,2,3])
    
    def findNearestNeighbours(self):

        self.up= np.roll(self.arr, -1, axis=0)
        self.down= np.roll(self.arr, +1, axis=0)
        self.right= np.roll(self.arr, +1, axis=1)
        self.left= np.roll(self.arr, -1, axis=1)

        self.neighbourList= [self.up[self.i], self.down[self.i], self.left[self.i], self.right[self.i]]
        self.neighbourIndex= [self.upIndex[self.i], self.downIndex[self.i], self.leftIndex[self.i], self.rightIndex[self.i]]


    def updateSite(self):

        if self.arr[self.i]== 0:
            pass
        if self.arr[self.i]== 1:
            self.chooseRandomNeighbour()
            if np.random.rand <= 1-self.p:
                self.arr[self.i]==0
            if np.random.rand <= self.p & self.neighbourList[self.randomNeighbourListIndex] == 0:
                randomNeighbourIndex= self.neighbourIndex[self.randomNeighbourListIndex]
                self.arr[randomNeighbourIndex] == 1            

    def updateLattice(self, arr):
        
        self.arr= arr
        self.generateRandomIndex()
        self.findNearestNeighbours()
        self.updateSite()

        return self.arr

