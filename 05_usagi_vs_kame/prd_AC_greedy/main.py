#!/usr/bin/env python3

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())
qs = list(map(int,input().split()))

A += [float('inf')]
B += [0]

ans = []
next_usa_move_t = 0
usa_masu = 0
for a,b in zip(A,B):
    next_usa_move_t += a
    while len(ans) < Q and qs[len(ans)] < next_usa_move_t:
        kame_masu = qs[len(ans)]
        if kame_masu < usa_masu:
            ans.append('usagi')
        elif kame_masu == usa_masu:
            ans.append('draw')
        else:
            ans.append('kame')
    usa_masu += b

print(*ans,sep='\n')
