#!/usr/bin/env python3
import random

MIN = 1
MAX = 1000

ALL_1_TESTCASES = 5
MANY_1_TESTCASES = 10
SINGLE_TESTCASES = 5
RANDOM_TESTCASES = 10

def ndwich(n):
    return '|' + (n-1) * '#|'
def random_sequence():
    ret = ''
    for i in range(10):
        ret += ndwich(random.randint(1,10))
    return ret
def random_many1_sequence():
    ret = ''
    for i in range(10):
        ret += ndwich(max(1, random.randint(-30,3)))
    return ret

testcases = set()

testcases.add('|#||#||#|#||#||||#|')
testcases.add('|')
testcases.add(ndwich(499))
testcases.add(ndwich(249)*2)
testcases.add(ndwich(1)*2)
testcases.add(ndwich(1) + ndwich(2))
testcases.add(ndwich(1) + ndwich(10))
testcases.add(ndwich(2) + ndwich(1))
testcases.add(ndwich(10) + ndwich(1))
testcases.add(ndwich(1)*100)
testcases.add(ndwich(2)*100)
testcases.add(ndwich(3)*100)
testcases.add(ndwich(1)*50 + ndwich(2)*50)
testcases.add(ndwich(2)*50 + ndwich(3)*50)
testcases.add(ndwich(3)*50 + ndwich(1)*50)
testcases.add((ndwich(1) + ndwich(2)) * 50)
testcases.add((ndwich(2) + ndwich(1)) * 50)
testcases.add((ndwich(1) + ndwich(2) + ndwich(1)) * 50)

all_1_cases = 0
many_1_cases = 0
single_cases = 0
random_cases = 0

while all_1_cases < ALL_1_TESTCASES:
    case = ndwich(1) * random.randint(MIN,MAX)
    if case in testcases: continue
    testcases.add(case)
    all_1_cases += 1
while many_1_cases < MANY_1_TESTCASES:
    case = ''
    while 1:
        add = random_many1_sequence()
        if len(case) + len(add) > MAX: break
        case += add
    if case in testcases: continue
    testcases.add(case)
    many_1_cases += 1
while single_cases < SINGLE_TESTCASES:
    r = random.randint(MIN,MAX)
    case = ndwich(r)
    if case in testcases: continue
    single_cases += 1
while random_cases < RANDOM_TESTCASES:
    case = ''
    while 1:
        add = random_sequence()
        if len(case) + len(add) > MAX: break
        case += add
    if case in testcases: continue
    testcases.add(case)
    random_cases += 1


for i, s in enumerate(list(testcases)):
    with open('input_{}.in'.format(i), 'w') as fout:
        fout.write(s)
