#!/usr/bin/env python3
from random import randint as ri

N_MAX = 499
N_MIN = 3
M_MAX = 10**6
M_MIN = 2

class Case:
    def __init__(self,N,M,A,B,label):
        self.N = N
        self.M = M
        self.A = A
        self.B = B
        self.label = label
    def __str__(self):
        ret = "{0} {1}".format(self.N,self.M) + '\n'
        ret += "{0} {1}".format(self.A,self.B) + '\n'
        return ret

def random_odd(lo,hi):
    r = ri(lo,hi)
    if r%2: return r
    if r+1 <= hi: return r+1
    if r-1 >= lo: return r-1
    raise ValueError('no odd integers between {1} and {2}'.format(lo,hi))

testcases = []
#sample cases
label = '00_sample'
testcases.append(Case(3, 3, 1, 2, label))
testcases.append(Case(5, 3, 2, 2, label))
testcases.append(Case(N_MAX, 500, 255, 243, label))

#impossible cases
label = '10_impossible'
testcases.append((Case(N_MIN, 3, 1, 3, label)))
testcases.append((Case(N_MIN, 3, 3, 1, label)))
testcases.append((Case(N_MIN, 4, 1, 4, label)))
testcases.append((Case(N_MIN, 4, 4, 1, label)))
testcases.append((Case(N_MIN, 3, 1, 3, label)))
testcases.append((Case(N_MIN, 3, 3, 1, label)))
testcases.append((Case(N_MIN, 3, 3, 1, label)))
testcases.append((Case(N_MAX, N_MAX, 1, N_MAX, label)))
testcases.append((Case(N_MAX, N_MAX, N_MAX, 1, label)))
testcases.append((Case(N_MAX, N_MAX+1, 1, N_MAX+1, label)))
testcases.append((Case(N_MAX, N_MAX+1, N_MAX+1, 1, label)))
testcases.append((Case(N_MAX, M_MAX, 100, M_MAX-100, label)))
testcases.append((Case(N_MAX, M_MAX, M_MAX-100, 100, label)))
testcases.append((Case(N_MAX, M_MAX, 1, N_MAX, label)))
testcases.append((Case(N_MAX, M_MAX, N_MAX, 1, label)))
testcases.append((Case(N_MAX, M_MAX, M_MAX-N_MAX+1, M_MAX, label)))
testcases.append((Case(N_MAX, M_MAX, M_MAX, M_MAX-N_MAX+1, label)))

RANDOM_WIDE_CASES = 10
RANDOM_NARROW_CASES = 10
RANDOM_ONE_SIDE_NARROW_CASES = 7

#wide cases
label = '20_wide'
testcases.append((Case(N_MIN, 100, 50, 50, label)))
testcases.append((Case(111, M_MAX, 33333, 33321, label)))
testcases.append((Case(333, M_MAX, 77777, 77700, label)))
testcases.append((Case(N_MAX, M_MAX, 55555, 55678, label)))
testcases.append((Case(N_MAX, M_MAX, 10000, 10000+N_MAX-2, label)))

label = '21_random_wide'
for _ in range(RANDOM_WIDE_CASES):
    ab_lower_lim = N_MAX+10
    ab_higher_lim = M_MAX-N_MAX-10
    A = ri(ab_lower_lim, ab_higher_lim)
    B = ri(max(ab_lower_lim, A-(N_MAX-4)), min(ab_higher_lim, A+(N_MAX-4)))
    N = random_odd(abs(A-B)+2, N_MAX)
    M = ri(max(A,B)+N_MAX, M_MAX)
    testcases.append(Case(N, M, A, B, label))

#narrow cases
label = '22_narrow'
testcases.append((Case(5, M_MIN, 1, 2, label)))
testcases.append((Case(111, 20, 5, 15, label)))
testcases.append((Case(333, 80, 7, 77, label)))
testcases.append((Case(N_MAX, M_MIN, 2, 2, label)))

label = '23_random_narrow'
for _ in range(RANDOM_NARROW_CASES):
    N = random_odd(N_MIN+2, N_MAX)
    M = ri(M_MIN, N//2+1)
    A = ri(1, M)
    B = ri(1, M)
    testcases.append(Case(N, M, A, B, label))

#left-narrow cases
label = '24_left_narrow'
testcases.append((Case(5, 80, 1, 2, label)))
testcases.append((Case(99, M_MAX, 33, 22, label)))
testcases.append((Case(111, M_MAX, 1, 1, label)))
testcases.append((Case(333, M_MAX, 100, 50, label)))

label = '25_random_left_narrow'
for _ in range(RANDOM_ONE_SIDE_NARROW_CASES):
    N = random_odd(N_MIN+2, N_MAX)
    M = ri(N, M_MAX)
    A = ri(1, N//2)
    B = ri(1, N//2)
    testcases.append(Case(N, M, A, B, label))

#right-narrow cases (symmetry of left-narrow cases)
right_narrow_cases = []
for case in testcases:
    if not case.label.endswith('left_narrow'): continue
    label = case.label.replace('left', 'right').replace('24','26').replace('25','27')
    right_narrow_cases.append(Case(case.N, case.M, case.M - case.A + 1, case.M - case.B + 1, label))
testcases += right_narrow_cases

#output
from collections import Counter
ctr = Counter()
for case in testcases:
    i = ctr[case.label]
    ctr[case.label] += 1
    with open('{0}_{1}.in'.format(case.label, i), 'w') as fout:
        fout.write(str(case))
