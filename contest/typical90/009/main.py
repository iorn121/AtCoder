from math import atan2, degrees
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


ans = 0
for p, (x0, y0) in enumerate(points):
    deg = [degrees(atan2(y1-y0, x1-x0))
           for q, (x1, y1) in enumerate(points) if p != q]
    deg.sort()

    i, j = 0, 1
    while j < N-1:
        tmp = deg[j]-deg[i]
        ans = max(ans, min(tmp, 360-tmp))
        if deg[j]-deg[i] < 180:
            j += 1
        else:
            i += 1
print(ans)
