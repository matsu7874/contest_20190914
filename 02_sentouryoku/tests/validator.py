#!/usr/bin/env python3

S = input()

assert 2 <= len(S) <= 10
assert all('A' <= c <= 'Z' for c in S)
