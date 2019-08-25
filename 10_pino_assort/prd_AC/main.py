#!/usr/bin/env python3

N,K = map(int,input().split())

V = []
A = []
C = []
no_fav = 0
for _ in range(N):
    v,a,c = map(int,input().split())
    if v > 1:
        V.append(v-1)
    elif a > 1:
        A.append(a-1)
    elif c > 1:
        C.append(c-1)
    else:
        no_fav += 1
V.sort()
A.sort()
C.sort()

def enough(n):
    v,a,c = n*10-K, n*7-K, n*7-K
    if v < 0 or a < 0 or c < 0:
        return False
    k = K - no_fav
    if k <= 0: return True
    for vi in V:
        if vi > v: break
        v -= vi
        k -= 1
        if k == 0: return True
    for ai in A:
        if ai > a: break
        a -= ai
        k -= 1
        if k == 0: return True
    for ci in C:
        if ci > c: break
        c -= ci
        k -= 1
        if k == 0: return True
    return False

ng = 0
ok = 10**7
while ok-ng > 1:
    m = (ok+ng)//2
    if enough(m):
        ok = m
    else:
        ng = m
print(ok)
