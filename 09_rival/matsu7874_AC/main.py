#!/usr/bin/env python
import heapq
import collections

L = 0
P = 1
R = 2


class SegmentTree:
    def __init__(self, size: int, identity=0):
        n_leaf = 1
        while n_leaf < size:
            n_leaf <<= 1
        self.n_leaf = n_leaf
        self.identity = identity
        self.data = [identity] * (2 * self.n_leaf - 1)

    def _query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.identity
        elif a <= l and r <= b:
            return self.data[k]
        else:
            m = (l+r) >> 1
            child_left = self._query(a, b, (k << 1)+1, l, m)
            child_right = self._query(a, b, (k << 1)+2, m, r)
            return child_left + child_right

    def query(self, a: int, b: int):
        """半開区間[a, b)のquery結果を返す。

        Args:
            a (int): index下限(含む)
            b (int): index上限(含まない)
        Returns:
            query_result (T)
        """
        return self._query(a, b, 0, 0, self.n_leaf)

    def add(self, index: int, value):
        """index番目の要素に値valueを加算する。

        Args:
            index (int): 更新対象のindex
            value (T): 更新する値T
        """
        i = index + self.n_leaf - 1
        self.data[i] += value
        while i > 0:
            i = (i - 1) >> 1
            self.data[i] += value


def main():
    n = int(input())
    gorillas = []
    commands = []
    values = set()
    for i in range(n):
        p, l, r = map(int, input().split())
        gorillas.append((p, l, r))
        commands.append((l, L, i))
        commands.append((p, P, i))
        commands.append((r, R, i))
        values.add(p)
        values.add(l)
        values.add(r)
    values = {v: i for i, v in enumerate(sorted(list(values)))}
    commands.sort()
    # ライバルゴリラの範囲分布を管理[l,r]

    total = 0
    acceptable = SegmentTree(len(values))
    for _, c, i in commands:
        if c == 0:
            # ライバル認定下限の低い順にセグ木に追加
            acceptable.add(values[gorillas[i][0]], 1)
        elif c == 1:
            l, r = gorillas[i][1], gorillas[i][2]
            total += acceptable.query(values[l], values[r]+1)
        else:
            acceptable.add(values[gorillas[i][0]], -1)
    print((total-n)//2)


if __name__ == "__main__":
    main()
