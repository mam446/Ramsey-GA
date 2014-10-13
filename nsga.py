# cython: profile=True
import pareto
import sys
import time
import random
import copy
import solution

def tournSelect(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj<best:
            best = obj
    return best

def nsga(params,setup,log=False):

    mu = params['mu']['value'] #100
    k = params['childK']['value'] #8

    pop = []
    i = 0

    nodes = setup['nodes'] #13

    m = setup['m'] # 3
    n = setup['n'] # 5
    alt = params['altMutate']['value'] #0.002

    s = solution.solution(nodes,m,n)
    si = solution.solution(nodes,m,n)
    for i in xrange(2,m):
        s.g.makeTuran(i)
        s.evaluate()
        pop.append(s)
    for i in xrange(2,n):
        si.g.makeInvTuran(i)
        si.evaluate()
        pop.append(si)
    print "Pre:"
    
    while i<mu:
        x = solution.solution(nodes,m, n) 
        x.evaluate()
        pop.append(x)
        i+=1
    pop.sort()
    print "Here"
    maxEvals = setup['evals'] #50000
    cur = mu
    children = params['lambda']['value']

    rate = params['rate']['value']

    sk = params['survK']['value']

    fronts = pareto.pareto(pop)



    while cur<maxEvals:
        
        
        childs = []
        for i in xrange(children):
            if random.random()<alt:
                x= None
                if random.choice([True,False]):
                    x = fronts.tournSelect(k).invert()
                else:
                    x = fronts.tournSelect(k).altMutate()
                x.evaluate()
                childs.append(x)
                continue
            x = fronts.tournSelect(k).mate(fronts.tournSelect(k))
            x.mutate(rate)
            x.evaluate()
            childs.append(x)
        cur += children
        survive = []

        pop = fronts.getPop()
        pop.extend(childs)
        fronts = pareto.pareto(pop)
        fronts.keepMu(mu)

        s = 0.0
        q = [1 for e in xrange((nodes*nodes-1)/2)]
        found = False
        c = 0
        for i in fronts.fronts[0]:
            q = [a and b for a,b in zip(q,i.g.adj)]
            s+= i.fitness
            if log:
                print c, i.fitness,i.mFit,i.nFit,i.distance
            if i.fitness==0.0:
                i.report()
                found = True
            c+=1
        if log:
            print
            print
        x =sorted(fronts.fronts[0],key = lambda x:x.fitness)[0]
        if log:
            print cur, x.nFit,x.mFit,x.fitness
            print "Reg:",zip(x.g.sets.keys(),[len(x.g.sets[key]) for key in x.g.sets])
            print "Inv:",zip(x.g.invSets.keys(),[len(x.g.invSets[key]) for key in x.g.invSets])
        if found:
            break
    return sorted(fronts.fronts[0],key = lambda x:x.fitness)[0].fitness





if __name__=="__main__":
    fp = open(sys.argv[1])
    fs = open(sys.argv[2])

    p = eval(fp.read())
    s = eval(fs.read()) 
    
    nsga(p,s,True)








