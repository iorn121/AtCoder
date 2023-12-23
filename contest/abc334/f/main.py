import math
from typing import Callable

class SegmentTree:
    def __init__(self, size: int, default: float, func: Callable[[float, float], float]):
        self.size = 2 ** (size - 1).bit_length()
        self.default = default
        self.data = [default] * (2 * self.size)
        self.func = func

    def build(self, array: list):
        for i in range(len(array)):
            self.data[i + self.size - 1] = array[i]
        for i in range(self.size - 2, -1, -1):
            self.data[i] = self.func(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, i: int, x: float):
        i += self.size - 1
        self.data[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.data[i] = self.func(self.data[2 * i + 1], self.data[2 * i + 2])

    def fold(self, l: int, r: int):
        l += self.size
        r += self.size
        left = self.default
        right = self.default
        while l < r:
            if l & 1:
                left = self.func(left, self.data[l - 1])
                l += 1
            if r & 1:
                r -= 1
                right = self.func(self.data[r - 1], right)
            l >>= 1
            r >>= 1
        return self.func(left, right)

def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx * dx + dy * dy)

def main():
    n, k = map(int, input().split())
    sx, sy = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.append([sx, sy])
    ans = dist(sx, sy, xy[0][0], xy[0][1])
    d = [0] * n
    for i in range(n):
        dir = dist(xy[i][0], xy[i][1], xy[i + 1][0], xy[i + 1][1])
        ret = dist(xy[i][0], xy[i][1], sx, sy) + dist(sx, sy, xy[i + 1][0], xy[i + 1][1])
        ans += dir
        d[i] = ret - dir
    segtree = SegmentTree(n + 1, float('inf'), min)
    segtree.build([float('inf')] * (n + 1))
    segtree.update(0, 0)
    for i in range(1, n + 1):
        segtree.update(i, segtree.fold(max(0, i - k), i) + d[i - 1])
    ans += segtree.fold(n - k, n + 1)
    print(ans)

if __name__ == "__main__":
    main()