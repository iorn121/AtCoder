
N = int(input())

xy = []
INF = 10**18
ans = 0

for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))

for i in range(2, N):
    x1, y1 = xy[i]
    for j in range(i):
        x2, y2 = xy[j]
        for k in range(j):
            x3, y3 = xy[k]
            if (y2-y1)*(x3-x1) != (x2-x1)*(y3-y1):
                ans += 1


print(ans)
