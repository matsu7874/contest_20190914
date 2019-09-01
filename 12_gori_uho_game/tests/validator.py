#!/usr/bin/env python3

N = int(input())
R = [input() for i in range(5)]
C = list(map(int,input().split()))

assert 1 <= N <= 10
assert len(R) == 5
assert all(len(row)==5 for row in R)
assert N == len(C)
assert all(1 <= c <= 8 for c in C)
assert all(all(c in 'GB.' for c in row) for row in R)
assert sum(row.count('G') for row in R) == 1
assert sum(row.count('B') for row in R) == N
