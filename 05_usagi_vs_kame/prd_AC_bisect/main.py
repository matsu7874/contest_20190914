#!/usr/bin/env python3

import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Q = int(input())
qs = list(map(int, input().split()))

cuma = [0]
for a in A:
    cuma.append(cuma[-1] + a)
cumb = [0]
for b in B:
    cumb.append(cumb[-1] + b)

ans = []
for q in qs:
    i = bisect.bisect(cuma, q)
    usa = cumb[i-1]
    if q < usa:
        ans.append('usagi')
    elif q == usa:
        ans.append('draw')
    else:
        ans.append('kame')

print(*ans, sep='\n')
