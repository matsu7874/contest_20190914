#!/usr/bin/env python3
from random import randint as ri, sample

N_MAX = 10
N_MIN = 1

class Case:
    def __init__(self,grid,cards,label):
        self.grid = grid
        self.cards = cards
        self.label = label
    def __str__(self):
        ret = str(len(self.cards)) + '\n'
        for row in self.grid:
            ret += row + '\n'
        ret += ' '.join(map(str,self.cards)) + '\n'
        return ret

testcases = []
#sample cases
label = 'sample'
testcases.append(Case([
    '.....',
    '.G.B.',
    '...BB',
    '.....',
    '.BB..'
], [3,1,4,1,5], label))
testcases.append(Case([
    'G.B..',
    '....B',
    '.....',
    'B...B',
    '.B...'
], [2,5,3,1,4], label))
testcases.append(Case([
    '.....',
    '.....',
    '.GB..',
    '.....',
    '.....'
], [8], label))
testcases.append(Case([
    'G.B..',
    'B..B.',
    'B.B..',
    'B....',
    'B....'
], [2,3,2,3,2,3,2], label))
testcases.append(Case([
    'B.B..',
    'B..B.',
    'GBB..',
    'B..B.',
    'B...B'
], [4,2,3,1,4,2,3,1,4,2], label))
testcases.append(Case([
    'GBB..',
    'B..B.',
    'B..B.',
    'BBB..',
    '.....'
], [1,2,3,1,2,3,1,2,3], label))

#other handmade cases
label = 'handmade'
testcases.append(Case([
    'G.B.B',
    '...B.',
    '..B..',
    '.B...',
    'B.B.B'
], [8,4,2,4,2,4,2,4], label))
testcases.append(Case([
    '..B..',
    '.B.B.',
    'B.G.B',
    'BBBBB',
    '.....'
], [1,2,3,4,5,6,7,8,8,8], label))
testcases.append(Case([
    'BB...',
    'G.B..',
    'BBBB.',
    'B.B..',
    'B....'
], [1,1,1,1,1,1,1,1,1,1], label))
testcases.append(Case([
    '.....',
    '..B..',
    '.BGB.',
    '..B..',
    '.....'
], [1,1,1,1], label))
testcases.append(Case([
    '....B',
    '...BB',
    '.BGB.',
    'BB...',
    'B....'
], [1,1,1,1,1,1,1,1], label))
testcases.append(Case([
    'GB...',
    '.BB..',
    '..BB.',
    '...BB',
    '....B'
], [8,7,6,5,4,3,2,1], label))
testcases.append(Case([
    '.....',
    '.G...',
    '.....',
    '...B.',
    '.....'
], [4], label))
testcases.append(Case([
    '.....',
    '.G...',
    '.B...',
    '.B...',
    '.B...'
], [4,4,4], label))

def make_random_case(n, label):
    grid = [['.']*5 for _ in range(5)]
    sel = sample(range(25), n+1)
    for i,r in enumerate(sel):
        y,x = divmod(r,5)
        grid[y][x] = 'G' if i==n else 'B'
    cards = []
    for _ in range(n):
        r1,r2 = sample(range(25), 2)
        y1,x1 = divmod(r1,5)
        y2,x2 = divmod(r2,5)
        d = abs(y1-y2) + abs(x1-x2)
        cards.append(d)
    return Case([''.join(row) for row in grid], cards, label)

label = 'random'
for n in range(N_MIN, N_MAX):
    testcases.append(make_random_case(n, label))

label = 'random_max'
for _ in range(30):
    testcases.append(make_random_case(N_MAX, label))

#output
from collections import Counter
ctr = Counter()
for case in testcases:
    i = ctr[case.label]
    ctr[case.label] += 1
    with open('{0}_{1}.in'.format(case.label, i), 'w') as fout:
        fout.write(str(case))
