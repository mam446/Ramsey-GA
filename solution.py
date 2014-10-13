import copy
import random
import graph
import math
global id
id = 0

class solution:

    def __init__(self,numNodes,m,n):
        self.m = m
        self.n = n
        self.g = graph.graph(numNodes)

        self.mFit = 0
        self.nFit = 0
        self.altFitness = 0
        self.fitness = 0
        
        self.distance = None

        for i in xrange(len(self.g.adj)):
            self.g.adj[i] = random.choice([0,1])


    def calcDistance(self,other):
        s = 0
        for i in xrange(len(self.g.adj)):
            s+=(self.g.adj[i]-other.g.adj[i])**2
        return math.sqrt(s)

    def duplicate(self):
        s = copy.deepcopy(self)
        s.mFit = 0
        s.nFit = 0
        s.fitness = 0
        s.altFitness = 0
        s.g.sets = {}
        s.g.invSets = {}
        return s

    def altMutate(self):
        s = self.duplicate() 
        s.g = s.g.rotate()
        return s
    
    def invert(self):
        s = self.duplicate()
        s.g = s.g.invert()
        return s

    def evaluate(self):
        self.g.runBK()
        self.g.runInvBK()

        self.fitness = 0
        self.altFitness = 0
        self.mFit = 0
        self.nFit = 0

        for key in self.g.sets:
            if int(key)>=self.m:
                self.fitness+=int(key)**2*len(self.g.sets[key])
                self.mFit+=int(key)*len(self.g.sets[key])
                self.altFitness +=int(key)**2*len(self.g.sets[key])

        for key in self.g.invSets:
            if int(key)>=self.n:
                self.fitness+=int(key)**2*len(self.g.invSets[key])
                self.nFit+=int(key)*len(self.g.invSets[key])
                self.altFitness +=int(key)**2*len(self.g.invSets[key])

        global id
        #print id
        id+=1


    def mate(self, other):
        x = solution(self.g.nodes,self.m,self.n)

        for i in xrange(len(self.g.adj)):
            x.g.adj[i] = random.choice([self,other]).g.adj[i]

        return x

    def mutate(self,rate):

        for i in xrange(len(self.g.adj)):
            if random.random()<rate:
                if self.g.adj[i] ==1:
                    self.g.adj[i] = 0
                else:
                    self.g.adj[i] = 1

    def report(self):

        print self.fitness
        print self.g.adj
        print "reg"
        for key in self.g.sets:
            if int(key)>=self.m:
                print self.g.sets[key] 
        print "inv"
        for key in self.g.invSets:
            if int(key)>=self.n:
                print self.g.invSets[key] 
        self.g.drawGraph("reg")
        self.g.drawGraph("inv",True)

    def __lt__(self,other):
        return self.fitness<other.fitness


    def dominate(self,other):
        if self.mFit<=other.mFit and self.nFit<other.nFit:
            return True
        if self.mFit<other.mFit and self.nFit<=other.nFit:
            return True
        return False




