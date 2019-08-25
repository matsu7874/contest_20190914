#!/usr/bin/env python3

N,K = map(int,input().split())
ices = [tuple(map(int,input().split())) for i in range(N)]

assert 1 <= N <= 10**5
assert 1 <= K <= 10**5
for v,a,c in ices:
    assert 1 <= v <= 100
    assert 1 <= a <= 100
    assert 1 <= c <= 100
    assert 2 in (v+a, a+c, c+v)
