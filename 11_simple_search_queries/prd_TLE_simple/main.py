#!/usr/bin/env python3

S = input()
Q = int(input())
qs = [input() for i in range(Q)]

ans = []
for q in qs:
    ans.append('YES' if q in S else 'NO')

print(*ans, sep='\n')
