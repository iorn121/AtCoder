import math
from decimal import Decimal
N = int(input())

points = []
for i in range(N):
    x, y = map(Decimal, input().split())
    points.append((x, y))
ans = 0
for i in range(N-1):
    x1, y1 = points[i]
    for j in range(i+1, N):
        x2, y2 = points[j]
        xx = x1-x2
        yy = y1-y2
        ans = max(ans, math.sqrt(xx**2+yy**2))

print(ans)
