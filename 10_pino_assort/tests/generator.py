#!/usr/bin/env python3
from random import randint as ri
from random import shuffle

N_MAX = 10**5
N_MIN = 1
V_MAX = 100
V_MIN = 1

class Case:
    def __init__(self,K,ps,label):
        self.K = K
        self.ps = ps
        self.label = label
        self.N = len(ps)
    def __str__(self):
        ret = "{0} {1}".format(self.N,self.K) + '\n'
        for v,a,c in self.ps:
            ret += "{0} {1} {2}".format(v,a,c) + '\n'
        return ret

testcases = []
#sample cases
label = 'sample'
testcases.append(Case(4, [
    (8,1,1),(1,4,1),(1,1,3),(1,2,1),(1,1,1),(99,1,1)
], label))
testcases.append(Case(5, [
    (1,100,1),(1,100,1),(1,100,1),(1,100,1),(1,100,1)
], label))
testcases.append(Case(5, [
    (100,1,1),(1,100,1),(1,1,100),(100,1,1),(1,100,1),(1,1,100),(100,1,1),(1,100,1),(1,1,100)
], label))
testcases.append(Case(1, [
    (1,1,1)
], label))

#other handmade cases
label = 'handmade'
testcases.append(Case(5, [
    (20,1,1),(1,1,70),(16,1,1),(1,5,1),(1,6,1),(1,1,2),(1,1,9)
], label))
testcases.append(Case(5, [
    (20,1,1),(10,1,1),(17,1,1),(1,15,1),(1,3,1),(1,1,8),(1,1,15)
], label))
testcases.append(Case(5, [
    (8,1,1),(6,1,1),(5,1,1),(1,10,1),(1,1,10),(1,45,1),(1,1,50)
], label))
testcases.append(Case(5, [
    (1,1,1),(1,1,1),(1,1,1),(1,20,1),(1,1,1),(1,1,1),(35,1,1)
], label))
testcases.append(Case(8, [
    (1,1,1),(1,1,1),(1,1,1),(1,20,1),(1,1,1),(1,1,1),(35,1,1),(1,1,1),(1,1,1)
], label))
testcases.append(Case(5, [
    (1,1,1),(1,1,1),(16,1,1),(1,10,1),(1,1,10),(1,14,1),(20,1,1)
], label))


def make_random_value_case(k,all_1,v,a,c,label):
    ps = []
    for _ in range(all_1):
        ps.append((1,1,1))
    for _ in range(v):
        ps.append((ri(V_MIN,V_MAX),1,1))
    for _ in range(a):
        ps.append((1,ri(V_MIN,V_MAX),1))
    for _ in range(c):
        ps.append((1,1,ri(V_MIN,V_MAX)))
    shuffle(ps)
    return Case(k,ps,label)

def make_fixed_value_case(k,all_1,v,a,c,value,label):
    ps = []
    for _ in range(all_1):
        ps.append((1,1,1))
    for _ in range(v):
        ps.append((value,1,1))
    for _ in range(a):
        ps.append((1,value,1))
    for _ in range(c):
        ps.append((1,1,value))
    shuffle(ps)
    return Case(k,ps,label)

label = 'all_1'
testcases.append(make_random_value_case(8,16,0,0,0,label))
testcases.append(make_random_value_case(32,32,0,0,0,label))
testcases.append(make_random_value_case(999,N_MAX,0,0,0,label))
testcases.append(make_random_value_case(N_MAX,N_MAX,0,0,0,label))

label = 'almost_1'
testcases.append(make_random_value_case(15,16,3,3,3,label))
testcases.append(make_random_value_case(16,16,3,3,3,label))
testcases.append(make_random_value_case(17,16,3,3,3,label))
testcases.append(make_random_value_case(20,16,3,3,3,label))
testcases.append(make_random_value_case(22,16,3,3,3,label))
testcases.append(make_random_value_case(25,16,3,3,3,label))
testcases.append(make_random_value_case(25,16,3,3,3,label))
testcases.append(make_random_value_case(N_MAX-5,N_MAX-9,3,3,3,label))

label = 'extreme'
testcases.append(make_fixed_value_case(N_MAX,0,N_MAX,0,0,V_MAX,label))
testcases.append(make_fixed_value_case(N_MIN,0,0,N_MAX,0,V_MAX,label))
testcases.append(make_fixed_value_case(50000,0,0,0,N_MAX,V_MAX,label))

label = 'balanced'
testcases.append(make_random_value_case(200,10,1000,700,700,label))
testcases.append(make_random_value_case(10000,10,10000,7000,7000,label))
testcases.append(make_random_value_case(20000,10,10000,7000,7000,label))

label = 'balanced_random'
for _ in range(8):
    x = ri(100, N_MAX//24)
    k = ri(N_MIN, x*24)
    testcases.append(make_random_value_case(k,0,x*10,x*7,x*7,label))

#output
from collections import Counter
ctr = Counter()
for case in testcases:
    i = ctr[case.label]
    ctr[case.label] += 1
    with open('{0}_{1}.in'.format(case.label, i), 'w') as fout:
        fout.write(str(case))
