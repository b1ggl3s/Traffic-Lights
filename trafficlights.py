import queue



class Vertex:

    def __init__(self, inAdjacencies, outAdjacencies):
        self.inAdjacencies = inAdjacencies
        self.outAdjacencies = outAdjacencies

class Intersection(Vertex):

    def getStrategies(self):
        (inN, inE, inS, inW) = (vertex for vertex in self.inAdjacencies)
        (outN, outE, outS, outW) = (vertex for vertex in self.outAdjacencies)

        strategies = [((inN, outS), (inS, outN)),
                           ((inW, outE), (inE, outW)),
                           ((inN, outE), (inS, outW)),
                           ((inE, outS), (inW, outN)),
                           ((inN, outW), (inS, outE)),
                           ((inE, outN), (inW, outS))]
        strategies = self.removeNullStrategies(strategies)
        return strategies

    def removeNullStrategies(self, strategies):
        return [strategy for strategy in strategies if None not in strategy[0] and None not in strategy[1]]
        

    def update(self):
        return

class RoadQueue:
    def __init__(self, destinationVertex):
        self.destinationVertex = destinationVertex
        self.q = queue.Queue()

class Road:

    def __init__(self, inVertex, outVertex):
        self.inVertex = inVertex
        self.outVertex = outVertex

    def createQueues(self):
        [RoadQueue(vertex) for vertex in self.outVertex.outAdjacencies]


class Car:

    def __init__(self, destination, redTime):
        self.destination = destination
        self.redTime = redTime
        self.instructionStack = []

    

    
