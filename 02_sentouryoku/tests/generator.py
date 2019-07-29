#!/usr/bin/env python3
import random

MIN_S = 2
MAX_S = 10

ALL_A_TESTCASES = 5
ALL_Z_TESTCASES = 5
SHORTEST_RANDOM_TESTCASES = 10
LONGEST_RANDOM_TESTCASES = 10
RANDOM_TESTCASES = 10

testcases = set()

testcases.add('FORCIA')
testcases.add('AA')
testcases.add('ZZZZZZZZZZ')

all_a_cases = 1
all_z_cases = 1
shortest_cases = 0
longest_cases = 0
random_cases = 0

def rand_char():
    return chr(random.randint(ord('A'), ord('Z')))
def rand_len():
    return random.randint(MIN_S, MAX_S)

while all_a_cases < ALL_A_TESTCASES:
    case = 'A' * rand_len()
    if case in testcases: continue
    testcases.add(case)
    all_a_cases += 1
while all_z_cases < ALL_Z_TESTCASES:
    case = 'Z' * rand_len()
    if case in testcases: continue
    testcases.add(case)
    all_z_cases += 1
while shortest_cases < SHORTEST_RANDOM_TESTCASES:
    case = rand_char() * MIN_S
    if case in testcases: continue
    testcases.add(case)
    shortest_cases += 1
while longest_cases < LONGEST_RANDOM_TESTCASES:
    case = rand_char() * MAX_S
    if case in testcases: continue
    testcases.add(case)
    longest_cases += 1
while random_cases < RANDOM_TESTCASES:
    case = rand_char() * rand_len()
    if case in testcases: continue
    testcases.add(case)
    random_cases += 1

for i, s in enumerate(list(testcases)):
    with open('input_{}.in'.format(i), 'w') as fout:
        fout.write(s)
