from math import gcd

N = int(input())

positions = []

for i in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))

s = set()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        xd, yd = x1-x2, y1-y2
        g = gcd(xd, yd)
        s.add((xd//g, yd//g))

print(len(s))
