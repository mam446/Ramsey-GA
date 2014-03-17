import random
import copy
import SGA
def randomize(p):
    for key in p:
        if p[key]['type']=='int':
            p[key]['value'] = random.randint(p[key]['range'][0],p[key]['range'][1])
        elif p[key]['type']=='float':
            p[key]['value'] = random.random() 

        else:
            raise "whaoh"

def evaluate(ind,setup):
    s = 0.0
    for i in xrange(setup['runs']):
        s+=SGA.SGA(ind['params'],setup)
    ind['fitness'] = s/setup['runs'] 

def uniRecomb(one,two):
    k = copy.deepcopy(one)

    p = k['params']
    for key in p:
        p[key]['value'] = random.choice([one,two])['params'][key]['value']

    k['params'] = p
    k['fitness'] = 0
    return k

def mutate(ind,rate):
    k= copy.deepcopy(ind)
    p = k['params']
    for key in p:
        if random.random()<rate:
            if p[key]['type']=='int':
                p[key]['value'] = random.randint(p[key]['range'][0],p[key]['range'][1])
            elif p[key]['type']=='float':
                p[key]['value'] = random.random() 

            else:
                raise "whaoh"
    k['params'] = p
    k['fitness'] = 0
    return k


def ktourn(pool,k):
    best = None
    for i in xrange(k):
        obj = random.choice(pool)
        if not best or obj['fitness']<best['fitness']:
            best =obj
    return best

setup = {
            'nodes':13,
            'm':3,
            'n':5,
            'evals':10000,
            'runs':5
        }

params = {
            'mu':{
                    'value':100,
                    'type':'int',
                    'range':(1,1000),
                },
            'childK':{
                    'value':8,
                    'type':'int',
                    'range':(1,800),
                },
            'altMutate':{
                    'value':0.002,
                    'type':'float',
                    'range':(0.0,1.0),
                },
            'lambda':{
                    'value':40,
                    'type':'int',
                    'range':(1,1000),
                },
            'rate':{
                    'value':.001,
                    'type':'float',
                    'range':(0,1.0),
                },
            'survK':{
                    'value':10,
                    'type':'int',
                    'range':(1,1000),
                },
        }


ind = { 'params':None,
        'fitness':0.0
}



mu = 50
lamb = 10
evals = 100
rate = .1
ck = 8
sk = 20
cur = 0

pop = []
for i in xrange(mu):
    x = copy.deepcopy(params)
    randomize(x)
    y = copy.deepcopy(ind)
    y['params'] = x
    evaluate(y,setup)
    pop.append(y)


while cur< evals:

    childs = []

    for i in xrange(lamb):
        ch = mutate(uniRecomb(ktourn(pop,ck),ktourn(pop,ck)),rate)
        evaluate(ch,setup)
        childs.append(ch)
    cur+=lamb
    survive = []
    for i in xrange(mu):
        survive.append(ktourn(pop+childs,sk))

    pop = survive
    sorted(pop,key=lambda k: k['fitness'])
    s = 0.0
    for i in pop:
        s+=i['fitness']
    print "                                                   ",pop[0]['fitness']
    print pop[0]
print "Final"
print pop[0]







































