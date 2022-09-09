import math
from collections import defaultdict


def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
if K == 1:
    exit(print("Infinity"))
cnt = [0]*(N+1)
for i, (x0, y0) in enumerate(XY):
    d = defaultdict(int)
    for j, (x1, y1) in enumerate(XY):
        if i == j:
            continue
        dx = x1-x0
        dy = y1-y0
        g = math.gcd(dx, dy)
        dx //= g
        dy //= g
        if dx < 0 or (dx == 0 and dy < 0):
            dx *= -1
            dy *= -1
        d[(dx, dy)] += 1
    for k, v in d.items():
        cnt[v+1] += 1
ans = 0
for i in range(K, N+1):
    ans += cnt[i]//i
print(ans)
