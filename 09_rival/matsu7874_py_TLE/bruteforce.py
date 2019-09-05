#!/usr/bin/env python


class Gorilla:
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r


def main():
    n = int(input())
    gs = []
    for _ in range(n):
        p, l, r = map(int, input().split())
        gs.append(Gorilla(p, l, r))
    cnt = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            if gs[i].l <= gs[j].p <= gs[i].r and gs[j].l <= gs[i].p <= gs[j].r:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
