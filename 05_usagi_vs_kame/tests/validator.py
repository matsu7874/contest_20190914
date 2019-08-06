#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Q = int(input())
qs = list(map(int, input().split()))

assert 1 <= N <= 10**5
assert 1 <= Q <= 10**5
assert len(A) == len(B) == N
assert len(qs) == Q
assert all(1 <= a <= 10**9 for a in A)
assert all(1 <= b <= 10**9 for b in B)
assert all(q1 < q2 for q1,q2 in zip(qs,qs[1:]))
assert 0 <= qs[0]
assert qs[-1] <= 10**14
