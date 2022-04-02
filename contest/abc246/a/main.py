from collections import defaultdict
xx, yy = defaultdict(int), defaultdict(int)
for i in range(3):
    x, y = map(int, input().split())
    xx[x] += 1
    yy[y] += 1
ans = []
for x, v in xx.items():
    if v == 1:
        ans.append(x)
for y, v in yy.items():
    if v == 1:
        ans.append(y)
print(*ans)
