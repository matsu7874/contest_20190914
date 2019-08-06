#!/usr/bin/env python3

N = int(input())
S = input()
Q = int(input())
qs = list(map(int, input().split()))

assert 1 <= N <= 10**5
assert N == len(S)
assert 1 <= Q <= 10**5
assert Q == len(qs)
assert all('A' <= c <= 'Z' for c in S)
assert all(1 <= q <= N*(N+1)//2 for q in qs)