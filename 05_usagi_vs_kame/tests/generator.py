#!/usr/bin/env python3
from random import randint as ri

ELEM_MIN = 1
ELEM_MAX = 10**9
ARRAY_MAX = 10**5
SMALL_SIZE = 1000

class Case:
    def __init__(self,A,B,Q):
        self.A = A
        self.B = B
        self.Q = Q
    def __str__(self):
        ret = str(len(self.A)) + '\n'
        ret += ' '.join(map(str, self.A)) + '\n'
        ret += ' '.join(map(str, self.B)) + '\n'
        ret += str(len(self.Q)) + '\n'
        ret += ' '.join(map(str, self.Q))
        return ret

testcases = set()
testcases.add(Case([2,3,1],[2,1,5],[0,1,2,5,6,7,8,100]))
testcases.add(Case(
    [1000000000,1000000000,1000000000,1,1],
    [1000000000,1000000000,1000000000,1000000000,1000000000],
    [334,2718281845,3141592653,5000000000,100000000000000]
))
testcases.add(Case([1,1,1,1,1],[1,1,1,1,1],list(range(10))))
testcases.add(Case([2,2,2,2,2],[2,2,2,2,2],list(range(10))))
testcases.add(Case([2,1,1,1,1],[1,1,1,1,1],list(range(10))))
testcases.add(Case([1,1,1,1,1],[2,1,1,1,1],list(range(10))))
testcases.add(Case([1,2,1,2,1],[2,1,2,1,2],list(range(10))))
testcases.add(Case([1,3,1,3,1],[3,1,3,1,3],list(range(10))))
testcases.add(Case([1,2,3,1,2],[3,1,2,3,1],list(range(10))))
testcases.add(Case([3,2,1,3,2],[1,3,2,1,3],list(range(10))))
testcases.add(Case([ELEM_MAX]*ARRAY_MAX, [ELEM_MAX]*ARRAY_MAX,
    list(range(ELEM_MAX, ELEM_MAX*ARRAY_MAX+1, ELEM_MAX))
))

DEADHEAT_SMALL_TESTCASES = 10
DEADHEAT_LARGE_TESTCASES = 5
RANDOM_SMALL_TESTCASES = 10
RANDOM_LARGE_TESTCASES = 5

def random_large_queries():
    q = [0]
    while len(q) < ARRAY_MAX - 1:
        r = ri(1,ELEM_MAX*2)
        if q[-1] + r > ELEM_MAX * ARRAY_MAX: break
        q.append(q[-1] + r)
    return q

for _ in range(DEADHEAT_SMALL_TESTCASES):
    A,B = [],[]
    for _ in range(SMALL_SIZE):
        p,q = ri(1,5), ri(1,5)
        A.append(p)
        B.append(q)
    testcases.add(Case(A,B,list(range(SMALL_SIZE*5 + 100))))

STEP = ELEM_MAX - 5
for _ in range(DEADHEAT_LARGE_TESTCASES):
    A,B = [],[]
    for _ in range(ARRAY_MAX - 1):
        p,q = ri(1,5), ri(1,5)
        A.append(STEP + p)
        B.append(STEP + q)
    testcases.add(Case(A,B,random_large_queries()))      

for _ in range(RANDOM_SMALL_TESTCASES):
    A,B = [],[]
    for _ in range(SMALL_SIZE):
        p,q = ri(ELEM_MIN, ELEM_MAX), ri(ELEM_MIN, ELEM_MAX)
        A.append(p)
        B.append(q)
    Q = [0]
    for _ in range(SMALL_SIZE):
        Q.append(Q[-1] + ri(ELEM_MIN, ELEM_MAX))
    testcases.add(Case(A,B,Q))

for _ in range(RANDOM_LARGE_TESTCASES):
    A,B = [],[]
    for _ in range(ARRAY_MAX - 1):
        p,q = ri(ELEM_MIN, ELEM_MAX), ri(ELEM_MIN, ELEM_MAX)
        A.append(p)
        B.append(q)
    testcases.add(Case(A,B,random_large_queries()))


for i, case in enumerate(list(testcases)):
    with open('input_{}.in'.format(i), 'w') as fout:
        fout.write(str(case) + '\n')
