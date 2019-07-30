#!/usr/bin/env python3

S = input()

ans = []
pan = 0
for a,b in zip(S,S[1:]):
    if a == '|':
        pan += 1
        if b == '|':
            ans.append(pan)
            pan = 0
ans.append(pan+1)

print(*ans)
