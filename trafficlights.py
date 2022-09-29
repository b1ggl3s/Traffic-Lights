import queue

#test


class Intersection:

    def __init__(self, inN, inE, inS, inW, outN, outE, outS, outE, strategies):
        self.inN = inN
        self.inE = inE
        self.inS = inS
        self.inW = inW
        self.outN = outN
        self.outE = outE
        self.outW = outW
        self.outS = outS
        self.strategies = [((inN, outS), (inS, outN)),
                           ((inW, outE), (inE, outW)),
                           ((inN, outE), (inS, outW)),
                           ((inE, outS), (inW, outN)),
                           ((inN, outW), (inS, outE)),
                           ((inE, outN), (inW, outS))]

    def update(self):
        return

    

class Road:


class Car:

    def __init__(self, destination, redTime):
        self.destination = destination
        self.redTime = redTime

    

    
