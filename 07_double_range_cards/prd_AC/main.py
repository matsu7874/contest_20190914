#!/usr/bin/env python3

R,C = map(int,input().split())
cards = [tuple(map(int,input().split())) for i in range(R)]
Q = int(input())
qs = [tuple(map(int,input().split())) for i in range(Q)]

imos = [[0]*(C+1) for i in range(R+1)]
for a,b,c,d,e,f,g,h in qs:
    imos[a-1][c-1] += 1
    imos[a-1][d] -= 1
    imos[b][c-1] -= 1
    imos[b][d] += 1
    imos[e-1][g-1] += 1
    imos[e-1][h] -= 1
    imos[f][g-1] -= 1
    imos[f][h] += 1

for i in range(R):
    for j in range(C-1):
        imos[i][j+1] += imos[i][j]
for i in range(C):
    for j in range(R-1):
        imos[j+1][i] += imos[j][i]

ans = 0
for irow,crow in zip(imos,cards):
    for i,c in zip(irow,crow):
        ans += (i%2)*c
print(ans)
