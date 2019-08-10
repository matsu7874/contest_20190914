#!/usr/bin/env python

s = input()
ret = []
pre = ''
cnt = 0
for c in s:
    if c == '|':
        if pre == '|':
            ret.append(str(cnt))
            cnt = 0
        cnt += 1
    pre = c
ret.append(str(cnt))

print(' '.join(ret))
