#!/usr/bin/env python3

import bisect

N = int(input())
S = input()
Q = int(input())
qs = list(map(int, input().split()))

bounds = [0]
for i in range(1,N+1):
    bounds.append(bounds[-1] + i)

ans = []
for q in qs:
    i = bisect.bisect(bounds, q-1)
    ai = q-bounds[i-1] - 1
    ans.append(S[ai])
print(*ans, sep='\n')