#!/usr/bin/env python


def solve(N, A, B, M, Q):
    usagi = 0
    t = 0
    i = 0
    for q in Q:
        while i < N and t + A[i] <= q:
            t += A[i]
            usagi += B[i]
            i += 1
        if usagi < q:
            print('kame')
        elif usagi > q:
            print('usagi')
        else:
            print('draw')


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = int(input())
    Q = list(map(int, input().split()))
    solve(N, A, B, M, Q)


if __name__ == "__main__":
    main()
