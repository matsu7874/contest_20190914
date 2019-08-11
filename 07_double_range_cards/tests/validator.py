#!/usr/bin/env python3

R,C = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(R)]
Q = int(input())
qs = [tuple(map(int,input().split())) for _ in range(Q)]

assert 1 <= R <= 500
assert 1 <= C <= 500
assert all(all(1 <= v <= 9 for v in row) for row in cards)
assert 0 <= Q <= 10**5
for qrow in qs:
    assert len(qrow) == 8
    a,b,c,d,e,f,g,h = qrow
    assert 1 <= a <= b <= R
    assert 1 <= c <= d <= C
    assert 1 <= e <= f <= R
    assert 1 <= g <= h <= C
