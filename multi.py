# cython: profile=True
import sys
import time
import random
import copy
import solution
import topFront 

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj<best:
            best = obj
    return best


mu = 100 
k = 8

pop = []
i = 0

nodes = 35 

m = 4
n = 6
top = topFront.topFront()

while i<mu:
    x = solution.solution(nodes,m, n) 
    x.evaluate()
    pop.append(x)
    i+=1
    top.push(x)
pop.sort()

maxEvals = 50000
cur = mu
children = 40

rate = .001

sk = 10


while cur<maxEvals:
    
    
    childs = []
    for i in xrange(children):
        x = ktourn(pop+top.top,k).mate(ktourn(pop+top.top,k))
        x.mutate(rate)
        x.evaluate()
        childs.append(x)
        top.push(x)
    cur += children
    survive = []

    for i in xrange(mu):
        survive.append(ktourn(pop+childs,sk))

    pop = survive

    pop.sort()
    s = 0.0
    for i in pop:
        s+= i.fitness

    print cur, s/len(pop),pop[0].fitness, "(",pop[0].mFit,",",pop[0].nFit,")",len(top.top)

pop.sort()
pop[0].report()















