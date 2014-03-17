# cython: profile=True
import sys
import time
import random
import copy
import solution

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj<best:
            best = obj
    return best

def SGA(params,setup):

    mu = params['mu']['value'] #100
    k = params['childK']['value'] #8

    pop = []
    i = 0

    nodes = setup['nodes'] #13

    m = setup['m'] # 3
    n = setup['n'] # 5
    alt = params['altMutate']['value'] #0.002


    while i<mu:
        x = solution.solution(nodes,m, n) 
        x.evaluate()
        pop.append(x)
        i+=1
    pop.sort()

    maxEvals = setup['evals'] #50000
    cur = mu
    children = params['lambda']['value']

    rate = params['rate']['value']

    sk = params['survK']['value']

    while cur<maxEvals:
        
        
        childs = []
        for i in xrange(children):
            if random.random()<alt:
                x= None
                if random.choice([True,False]):
                    x = ktourn(pop,k).invert()
                else:
                    x = ktourn(pop,k).altMutate()
                x.evaluate()
                childs.append(x)
                continue
            x = ktourn(pop,k).mate(ktourn(pop,k))
            x.mutate(rate)
            x.evaluate()
            childs.append(x)
        cur += children
        survive = []

        for i in xrange(mu):
            survive.append(ktourn(pop+childs,sk))

        pop = survive

        pop.sort()
        s = 0.0
        q = [1 for e in xrange((nodes*nodes-1)/2)]
        for i in pop:
            q = [a and b for a,b in zip(q,i.g.adj)]
            s+= i.fitness
        if pop[0].fitness==0.0:
            pop[0].report()
            break
        print cur, s/len(pop),pop[0].fitness,pop[0].altFitness

    pop.sort()

    return pop[0].fitness













