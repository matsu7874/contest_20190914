#!/usr/bin/env python3

S = input()
Q = int(input())
qs = [input() for i in range(Q)]

assert 1 <= len(S) <= 30000
assert all('a' <= c <= 'z' for c in S)
assert 1 <= Q <= 10**5
assert Q == len(qs)
sumlen = 0
for q in qs:
    assert all('a' <= c <= 'z' for c in q)
    assert len(q) >= 1
    sumlen += len(q)
assert 1 <= sumlen <= 10**5
