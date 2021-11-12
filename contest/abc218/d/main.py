from collections import Counter

N = int(input())

xy = []

for i in range(N):
    x, y = map(int, input().split())
    xy.append((x, y))


xy.sort()
yyList = []

for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if x1 == x2:
            yyList.append((y1, y2))

yyDict = Counter(yyList)

ans = 0

for key, count in yyDict.items():
    if count > 1:
        ans += count*(count-1)//2
print(ans)
