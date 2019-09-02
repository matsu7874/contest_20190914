#!/usr/bin/env python3
from random import randint as ri

N_MAX = 1000
N_MIN = 1
Q_MAX = 10**6
Q_MIN = 1
SUM_MAX = 10**6

class Case:
    def __init__(self,S,qs,label):
        self.S = S
        self.qs = qs
        self.label = label
    def __str__(self):
        ret = self.S + '\n'
        ret += str(len(self.qs)) + '\n'
        for q in self.qs:
            ret += q + '\n'
        return ret

def random_letter(fr='a', to='z'):
    i = ri(0, ord(to)-ord(fr))
    return chr(ord(fr) + i)

def random_letters(n, fr='a', to='z'):
    ret = ''
    for _ in range(n):
        ret += random_letter(fr, to)
    return ret

testcases = []
#sample cases
label = 'sample'
testcases.append(Case('yurufuwacontest', [
    'yurufuwacon',
    'yuruyuru',
    'fuwafuwa',
    'ac',
    'wa',
    'contest',
    'contestttt',
    'goriiiiiiii'
], label))
testcases.append(Case('okomenooishiitakikatasoshiteokomewotaberukotoniyorusonokouka', [
    'okome',
    'okomekome',
    'bitamin',
    'mineraru',
    'shokumotsusenni'
], label))

#extreme cases
label = 'extreme'
testcases.append(Case('a'*N_MAX,
    ['a'*(N_MAX-1) + random_letter()] * (SUM_MAX // N_MAX),
label))
testcases.append(Case('a'*N_MAX,
    [random_letters(N_MAX)] * (SUM_MAX // N_MAX),
label))
s = random_letters(N_MAX)
testcases.append(Case(s,
    [s] * (SUM_MAX // N_MAX),
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(N_MAX - 1) + 'b'] * (SUM_MAX//N_MAX),
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(SUM_MAX//2000 - 1) + 'b'] * 2000,
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(SUM_MAX//5000 - 1) + 'b'] * 5000,
label))
testcases.append(Case('a'*N_MAX,
    ['b'] * Q_MAX,
label))
testcases.append(Case(random_letters(N_MAX,'a','c'),
    [random_letters(5, 'd', 'z') for _ in range(SUM_MAX // 5)],
label))
testcases.append(Case(random_letters(N_MAX),
    [random_letters(5) for _ in range(SUM_MAX // 5)],
label))

# TODO other cases

#output
from collections import Counter
ctr = Counter()
for case in testcases:
    i = ctr[case.label]
    ctr[case.label] += 1
    with open('{0}_{1}.in'.format(case.label, i), 'w') as fout:
        fout.write(str(case))
