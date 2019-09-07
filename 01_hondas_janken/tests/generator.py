#!/usr/bin/env python3
import random

SAME_TESTCASES = 10
DIFF_TESTCASES = 10

testcases = []

testcases.append('AC')
testcases.append('ZZ')

samecases = 1
diffcases = 1

def rand_char():
    return chr(random.randint(ord('A'), ord('Z')))

while samecases < SAME_TESTCASES:
    case = rand_char()*2
    if case in testcases: continue
    testcases.append(case)
    samecases += 1

while diffcases < DIFF_TESTCASES:
    r1, r2 = rand_char(), rand_char()
    if r1 == r2: continue
    case = r1+r2
    if case in testcases: continue
    testcases.append(case)
    diffcases += 1

for i, s in enumerate(list(testcases)):
    with open('input_{:03d}.in'.format(i), 'w') as fout:
        fout.write(s + '\n')
