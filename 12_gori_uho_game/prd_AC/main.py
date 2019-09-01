#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N = int(input())
grid = [input() for _ in range(5)]
C = list(map(int,input().split()))

bs = []
for y,row in enumerate(grid):
    for x,c in enumerate(row):
        if c=='G':
            gx,gy = x,y
        elif c=='B':
            bs.append((x,y))
bs.append((gx,gy))

es = [defaultdict(lambda:[]) for _ in range(N+1)]

for i in range(N):
    ix,iy = bs[i]
    for j in range(i+1,N+1):
        jx,jy = bs[j]
        d = abs(ix-jx) + abs(iy-jy)
        es[i][d].append(j)
        es[j][d].append(i)

def judge(bits,i):
    ci = bin(bits).count('1')
    if ci==N: return 0
    d = C[ci]
    if not es[i][d]: return 0
    for j in es[i][d]:
        if j == N: continue
        if bits&(1<<j): continue
        if judge(bits|(1<<j), j) == 0:
            return 1
    return 0

print('gori' if judge(0,N) else 'uho')
