#!/usr/bin/env python3
import sys
input = sys.stdin.readline
S = input().rstrip()
Q = int(input())
qs = [input().rstrip() for _ in range(Q)]

N = len(S)
sa = [i for i in range(N+1)]
rank = [ord(c) for c in S] + [-1]

k = -1
key = lambda i: (rank[i], rank[i+k] if i+k <= N else -1)

def construct_sa():
    global k,rank
    k = 1
    tmp = [0] * (N+1)
    while k <= N:
        sa.sort(key=key)
        tmp[sa[0]] = 0
        for i in range(1,N+1):
            tmp[sa[i]] = tmp[sa[i-1]] + (key(sa[i-1]) < key(sa[i]))
        rank = [r for r in tmp]
        k *= 2

construct_sa()

ans = []
for q in qs:
    n = len(q)
    if n > N:
        ans.append('NO')
        continue
    l,r = 0,N
    while r-l > 1:
        m = (l+r)//2
        if S[sa[m]:sa[m]+n] < q:
            l = m
        else:
            r = m
    if S[sa[r]:sa[r]+n] == q:
        ans.append('YES')
        continue
    elif S[sa[r]:sa[r]+n] < q:
        ans.append('NO')
        continue
    while r <= N:
        if sa[r]+n <= N:
            ans.append(S[sa[r]:sa[r]+n])
            break
        r += 1
    else:
        ans.append('NO')

print(*ans, sep='\n')
