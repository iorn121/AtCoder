import sys
from typing import Callable

def optimize(low: int, high: int, f: Callable[[int], int]) -> int:
    while high - low > 2:
        m1 = (low + high) // 2
        m2 = m1 + 1
        if f(m1) < f(m2):
            low = m1
        else:
            high = m2
    return f(low + 1)

def solve():
    n, m = map(int, input().split())
    a = 0
    b = 0
    ans = -sys.maxsize
    for _ in range(n):
        x, y = map(int, input().split())
        f = lambda k: a + b * k + x * k * (k + 1) // 2
        if x > 0:
            ans = max(ans, f(1))
            ans = max(ans, f(y))
        else:
            ans = max(ans, optimize(0, y + 1, f))
        a = f(y)
        b += x * y
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()