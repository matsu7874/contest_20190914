#!/usr/bin/env python3
from random import randint as ri

N_MAX = 30000
N_MIN = 1
Q_MAX = 10**5
Q_MIN = 1
SUM_MAX = 10**5

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
label = '00_sample'
testcases.append(Case('abracadabra', [
    'abra',
    'cadabra',
    'brabra',
    'abura',
    'banana',
    'gorilla',
    'zebra',
    'a',
    'chocolate',
    'rarara',
    'aaaaaaaaaaa',
    'aaaaaaaaaaaa'
], label))
testcases.append(Case('yurufuwaonsite', [
    'yuru',
    'fuwa',
    'onsite',
    'gorira',
    'no',
    'chosenjo',
    'thank',
    'you',
    'for',
    'coming'
], label))

#other handmade cases
label = '10_handmade'
testcases.append(Case('abracadabra', [
    'abracadabqz',
    'abracadabra',
    'abracadabrb',
    'racadabqz',
    'racadabra',
    'racadabrb',
    'qz',
    'ra',
    'rb',
    'abqz',
    'abra',
    'abrb',
    'acadabqz',
    'acadabra',
    'acadabrb',
    'cadaa',
    'cadab',
    'cadac',
    'cadabqz',
    'cadabra',
    'cadabrb'
], label))
queries = []
for i in range(1,13):
    queries.append('a' * i)
    queries.append('b' * i)
    queries.append('r' * i)
testcases.append(Case('abracadabra', queries, label))


#extreme cases
label = '11_extreme'
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
    ['a'*(SUM_MAX//500 - 1) + 'b'] * 500,
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(SUM_MAX//2000 - 1) + 'b'] * 2000,
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(SUM_MAX//5000 - 1) + 'b'] * 5000,
label))
testcases.append(Case('a'*N_MAX,
    ['a'*(SUM_MAX//20000 - 1) + 'b'] * 20000,
label))
testcases.append(Case('a'*N_MAX,
    ['b'] * Q_MAX,
label))
testcases.append(Case(random_letters(N_MAX,'a','b'),
    [random_letters(5,'a','b') for _ in range(SUM_MAX // 5)],
label))
testcases.append(Case(random_letters(N_MAX,'a','c'),
    [random_letters(5,'a','c') for _ in range(SUM_MAX // 5)],
label))
testcases.append(Case('aaaab' * (N_MAX//5 - 5) + 'aaaaz',
    ['aaaa' + random_letter() for _ in range(SUM_MAX // 5)],
label))
queries,sumlen = ['a'],1
while sumlen + len(queries[-1]) + 1 <= SUM_MAX:
    queries.append(queries[-1] + 'a')
    sumlen += len(queries[-1])
testcases.append(Case('a'*N_MAX,
    queries,
label))

#large 'YES' cases
def large_yes_case():
    S = random_letters(N_MAX)
    queries = []
    sumlen = 0
    while 1:
        l = ri(1,len(S))
        if sumlen + l > SUM_MAX: break
        sumlen += l
        a = ri(0,N_MAX - l)
        q = S[a:a+l]
        queries.append(q)
    return Case(S, queries, '20_large_yes')

for _ in range(5):
    testcases.append(large_yes_case())

#large 'kiwadoi' cases
def large_kiwadoi_case():
    S = random_letters(N_MAX)
    queries = []
    sumlen = 0
    while 1:
        l = ri(1,len(S))
        if sumlen + l > SUM_MAX: break
        sumlen += l
        a = ri(0,N_MAX - l)
        q = S[a:a+l-1] + random_letter() #クエリの末尾をランダムに変更
        queries.append(q)
    return Case(S, queries, '21_large_kiwadoi')

for _ in range(5):
    testcases.append(large_kiwadoi_case())

# 命名がひどい
def large_kiwadoi2_case():
    S = random_letters(N_MAX)
    queries = []
    sumlen = 0
    while 1:
        l = ri(1,len(S))
        if sumlen + l > SUM_MAX: break
        sumlen += l
        a = ri(0,N_MAX - l)
        b = ri(0,l-1)
        q = S[a:a+b] + random_letter() + S[a+b+1:a+l] #クエリのどこか1文字をランダムに変更
        queries.append(q)
    return Case(S, queries, '22_large_kiwadoi2')

for _ in range(5):
    testcases.append(large_kiwadoi2_case())

#output
from collections import Counter
ctr = Counter()
for case in testcases:
    i = ctr[case.label]
    ctr[case.label] += 1
    with open('{0}_{1}.in'.format(case.label, i), 'w') as fout:
        fout.write(str(case))
