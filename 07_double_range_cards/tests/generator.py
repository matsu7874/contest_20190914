#!/usr/bin/env python3
from random import randint as ri

RC_MAX = 500
Q_MAX = 10**5
V_MIN = 1
V_MAX = 9
SMALL_RC = 100
SMALL_Q = 1000

class Case:
    def __init__(self,V,Q):
        self.V = V
        self.R = len(V)
        self.C = len(V[0])
        self.Q = Q
    def __str__(self):
        ret = "{0} {1}".format(self.R,self.C) + '\n'
        for vrow in self.V:
            ret += ' '.join(map(str, vrow)) + '\n'
        ret += str(len(self.Q)) + '\n'
        for qrow in self.Q:
            ret += ' '.join(map(str, qrow)) + '\n'
        return ret

testcases = []
testcases.append(Case(
    [[1,7,9,3], [6,5,4,8], [2,9,1,5]],
    [[1,2,1,3,2,3,2,4]]
))
testcases.append(Case(
    [[1]*5 for _ in range(5)],
    [[3,3,1,5,1,5,3,3], [1,2,1,2,4,5,4,5], [1,4,2,5,1,4,2,5], [1,3,1,3,3,3,3,3]]
))
testcases.append(Case([[1]], []))

def rand_pair(max_v):
    a = ri(1,max_v)
    b = ri(a,max_v)
    return (a,b)

def make_random_case(r_size,c_size,q_size):
    cards = []
    for r in range(r_size):
        row = []
        for c in range(c_size):
            row.append(ri(V_MIN, V_MAX))
        cards.append(row)
    queries = []
    for q in range(q_size):
        row = []
        for _ in range(2):
            a,b = rand_pair(r_size)
            row += [a,b]
            c,d = rand_pair(c_size)
            row += [c,d]
        queries.append(row)
    return Case(cards, queries)

testcases.append(make_random_case(1,1,0))
testcases.append(make_random_case(1,RC_MAX,0))
testcases.append(make_random_case(RC_MAX,1,0))
testcases.append(make_random_case(RC_MAX,RC_MAX,0))

testcases.append(make_random_case(1,1,1))
testcases.append(make_random_case(1,RC_MAX,1))
testcases.append(make_random_case(RC_MAX,1,1))
testcases.append(make_random_case(RC_MAX,RC_MAX,1))

for i in range(10):
    testcases.append(make_random_case(SMALL_RC,SMALL_RC,SMALL_Q))
for i in range(10):
    testcases.append(make_random_case(RC_MAX,RC_MAX,SMALL_Q))
for i in range(10):
    testcases.append(make_random_case(SMALL_RC,SMALL_RC,Q_MAX))
for i in range(5):
    testcases.append(make_random_case(RC_MAX,RC_MAX,Q_MAX))

for i, case in enumerate(list(testcases)):
    with open('input_{:03d}.in'.format(i), 'w') as fout:
        fout.write(str(case))
