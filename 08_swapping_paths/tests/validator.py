#!/usr/bin/env python3

N,M = map(int,input().split())
A,B = map(int,input().split())

assert 3 <= N <= 499
assert N%2 == 1
assert 2 <= M <= 10**6
assert 1 <= A <= M
assert 1 <= B <= M
