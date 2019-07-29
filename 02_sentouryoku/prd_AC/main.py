#!/usr/bin/env python3

S = input()
ans = 1
for a,b in zip(S,S[1:]):
    x = ord(a) - ord('A') + 1
    y = ord(b) - ord('A') + 1
    ans *= (x+y)
print(ans)
