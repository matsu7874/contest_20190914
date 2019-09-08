#!/usr/bin/env python3
import sys
input = sys.stdin.readline

N = int(input())
PLR = [tuple(map(int,input().split())) for _ in range(N)]

MAXP = 1003
imoses = [[0]*MAXP for _ in range(MAXP)]
for p,l,r in PLR:
    imoses[p][l] += 1
    imoses[p][r+1] -= 1
for i in range(MAXP):
    for j in range(MAXP-1):
        imoses[i][j+1] += imoses[i][j]

cum_rivals = [[0] for _ in range(MAXP)]
for i,rivals in enumerate(zip(*imoses)):
    for r in rivals:
        cum_rivals[i].append(cum_rivals[i][-1] + r)

ans = 0
for p,l,r in PLR:
    ans += cum_rivals[p][r+1] - cum_rivals[p][l]
print((ans-N) // 2)
