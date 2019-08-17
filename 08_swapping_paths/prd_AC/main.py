#!/usr/bin/env python3

N,M = map(int,input().split())
A,B = map(int,input().split())
MOD = 10**9+7

A,B = A-1,B-1
if A>B:
    A,B = B,A

if B-A >= N-1:
    print(0)
    exit()

H = N//2 + 1

if A > H:
    d = A-H
    A -= d
    B -= d
    M -= d

W = min(B+H, M)

dp1 = [[0]*W for _ in range(H)]
dp2 = [[0]*W for _ in range(H)]
dp1[0][A] = 1
dp2[0][B] = 1

for i in range(H-1):
    for j in range(W):
        if j > 0:
            dp1[i+1][j] += dp1[i][j-1]
            dp2[i+1][j] += dp2[i][j-1]
        dp1[i+1][j] += dp1[i][j]
        dp2[i+1][j] += dp2[i][j]
        if j < W-1:
            dp1[i+1][j] += dp1[i][j+1]
            dp2[i+1][j] += dp2[i][j+1]
        dp1[i+1][j] %= MOD
        dp2[i+1][j] %= MOD

dp = [a*b for a,b in zip(dp1[-1], dp2[-1])]

ans = 0
for i in range(W):
    for j in range(W):
        if i==j: continue
        ans += dp[i] * dp[j]
        ans %= MOD
print(ans)
