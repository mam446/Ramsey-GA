import random
from pygraphviz import *
import copy




class graph:

    def duplicate(self):
        g = copy.deepcopy(self)

        g.sets = {}
        g.invSets = {}
        return g

    def rotate(self):
        g = self.duplicate()
        i = random.randint(0,self.nodes-1)
        j = random.randint(0,self.nodes-1)
        for k in xrange(self.nodes):
            if i!=k and j!=k:
                g.adj[g.getLoc(i,k)] = self.at(j,k)
                g.adj[g.getLoc(j,k)] = self.at(i,k)
        return g

    def __init__(self,numNodes):
        self.adj = [0 for i in xrange(numNodes*(numNodes-1)/2)]
        self.nodes = numNodes
        self.sets = {}
        
        self.knownLabels = [None for i in xrange(numNodes)]
        self.invSets = {}

    def at(self,j,k):
        return self.adj[self.getLoc(j,k)]

    def getLoc(self,j,k): 
        small = min(j,k)
        big = max(j,k)
        if big == small:
            return None
        return big*(big-1)/2+small

    def runBK(self):
        self.sets = {}
        self.bronKerbosch(set(),set([i for i in xrange(self.nodes)]),set())


    def invert(self):
        g = self.duplicate()
        
        for i in xrange(len(g.adj)):
            if g.adj[i] == 1:
                g.adj[i] = 0
            else:
                g.adj[i] = 1
        return g
    
    def runInvBK(self):
        self.invSets = {}
        for i in xrange(len(self.adj)):
            if self.adj[i] == 1:
                self.adj[i] = 0
            else:
                self.adj[i] = 1


        self.bronKerbosch(set(),set([i for i in xrange(self.nodes)]),set(),True)


        for i in xrange(len(self.adj)):
            if self.adj[i] == 1:
                self.adj[i] = 0
            else:
                self.adj[i] = 1

    def bronKerbosch(self,R, P, X,inv = False):
        if not P and not X :
            if not inv:
                if len(R) not in self.sets:
                    self.sets[len(R)] = []
                self.sets[len(R)].append(R)
            else:
                if len(R) not in self.invSets:
                    self.invSets[len(R)] = []
                self.invSets[len(R)].append(R)

        i = 0
        cP = set(P)
        for v in cP:
            n = self.neigh(v)
            self.bronKerbosch(R.union([v]),P.intersection(n),X.intersection(n),inv)
            P.discard(v)
            X.add(v)

    def neigh(self,node):
        ret = []
        for i in xrange(self.nodes):
            if i == node:
                continue
            if self.at(node,i):
                ret.append(i)
        return ret
















    def drawGraph(self,name,inv=False,known=True):
        l = None
        if known:
            l = self.knownLabels
        else:
            l = self.calcLabels
        if inv:
            for i in xrange(len(self.adj)):
                if self.adj[i] == 1:
                    self.adj[i] = 0
                else:
                    self.adj[i] = 1


        A = AGraph()

        A.node_attr['style'] = 'filled'
        A.node_attr['shape'] = 'circle'

        
        A.node_attr['fixedsize'] = 'false'
        
        colors = ['red','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle''red','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle''red','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle''red','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle''red','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle','green','blue','orange','yellow','purple','sienna','mediumaquamarine','orchid','palegreen2','pink','slateblue4','yellow4','tomato','thistle']

        classes = {}

        for i in xrange(self.nodes):
            
            classes[l[i]] = None


        for i in xrange(self.nodes):
            A.add_node(i)
            n = A.get_node(i)
            n.attr['label'] = i
            n.attr['fillcolor'] = colors[classes.keys().index(l[i])]
            if l[i]==None:
                n.attr['fillcolor'] = 'grey'       
        
        for i in xrange(self.nodes):
            for j in xrange(i):
                if self.at(i,j):
                    A.add_edge(i,j,len= 2.5)

        A.layout()
        A.write(name+'.dot')
        A.draw(name+'.png')

        return None
