#!/usr/bin/env python3
from random import randint as ri

S_SIZE = Q_SIZE = 10**5
SMALL_SIZE = 1000

class Case:
    def __init__(self,S,Q):
        self.S = S
        self.Q = Q
    def __str__(self):
        ret = str(len(self.S)) + '\n'
        ret += self.S + '\n'
        ret += str(len(self.Q)) + '\n'
        ret += ' '.join(map(str, self.Q))
        return ret

testcases = set()
testcases.add(Case('ABCA', [2,6,10]))
testcases.add(Case('Z', [1]))

def make_ordered_str(l):
    ret = ''
    while len(ret) < l:
        i = len(ret)%26
        ret += chr(ord('A') + i)
    return ret

def make_random_str(l):
    ret = ''
    while len(ret) < l:
        i = ri(0,25)
        ret += chr(ord('A') + i)
    return ret

def make_random_query(l,maxv):
    ret = []
    while len(ret) < l:
        ret.append(ri(1,maxv))
    return ret

START_QUERY_RANDOM_STR_SMALL_TESTCASES = 10
END_QUERY_RANDOM_STR_SMALL_TESTCASES = 10
RANDOM_QUERY_ORDERED_STR_LARGE_TESTCASES = 5
RANDOM_QUERY_RANDOM_STR_LARGE_TESTCASES = 5

for _ in range(START_QUERY_RANDOM_STR_SMALL_TESTCASES):
    S = make_random_str(SMALL_SIZE)
    Q = list(range(1,SMALL_SIZE+1))
    testcases.add(Case(S,Q))

for _ in range(END_QUERY_RANDOM_STR_SMALL_TESTCASES):
    S = make_random_str(SMALL_SIZE)
    end = SMALL_SIZE*(SMALL_SIZE+1)//2
    Q = list(range(end, end-SMALL_SIZE, -1))
    testcases.add(Case(S,Q))

for _ in range(RANDOM_QUERY_ORDERED_STR_LARGE_TESTCASES):
    S = make_ordered_str(S_SIZE)
    n = len(S)
    Q = make_random_query(Q_SIZE, n*(n+1)//2)
    testcases.add(Case(S,Q))

for _ in range(RANDOM_QUERY_RANDOM_STR_LARGE_TESTCASES):
    S = make_random_str(S_SIZE)
    n = len(S)
    Q = make_random_query(Q_SIZE, n*(n+1)//2)
    testcases.add(Case(S,Q))

for i, case in enumerate(list(testcases)):
    with open('input_{}.in'.format(i), 'w') as fout:
        fout.write(str(case) + '\n')
