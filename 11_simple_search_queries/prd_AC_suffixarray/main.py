#!/usr/bin/env python3
import sys
input = sys.stdin.readline
from bisect import bisect_left

S = input().rstrip()
Q = int(input())
qs = [input().rstrip() for i in range(Q)]

suffix_arr = [S[i:] for i in range(len(S))]
suffix_arr.sort()

ans = []
for q in qs:
    i = bisect_left(suffix_arr, q)
    if i == len(S):
        ans.append('NO')
        continue
    ans.append('YES' if suffix_arr[i].startswith(q) else 'NO')

print(*ans, sep='\n')
