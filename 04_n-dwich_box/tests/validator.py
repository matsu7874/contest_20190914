#!/usr/bin/env python3

S = input()

assert 1 <= len(S) <= 1000
assert all(c in '|#' for c in S)
assert '##' not in S
assert S[0] == S[-1] == '|'
