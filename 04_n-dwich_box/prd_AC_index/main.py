#!/usr/bin/env python3

S = input()

ids = []
for i,c in enumerate(S):
    if c == '#':
        ids.append(i)

if len(ids) == 0:
    print(*([1] * len(S)))
    exit()

ans = [1] * (ids[0] - 1)
lev = 2
for i,j in zip(ids,ids[1:]):
    if j-i == 2:
        lev += 1
    else:
        ans.append(lev)
        ans += [1] * (j-i-3)
        lev = 2

ans.append(lev)
ans += [1] * (len(S) - ids[-1] - 2)

print(*ans)
