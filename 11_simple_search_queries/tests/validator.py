#!/usr/bin/env python3

S = input()
Q = int(input())
qs = [input() for i in range(Q)]

assert 1 <= len(S) <= 1000
assert all('a' <= c <= 'z' for c in S)
assert 1 <= Q <= 10**6
assert Q == len(qs)
sumlen = 0
for q in qs:
    assert all('a' <= c <= 'z' for c in q)
    assert len(q) <= len(S)
    sumlen += len(q)
assert 1 <= sumlen <= 10**6
