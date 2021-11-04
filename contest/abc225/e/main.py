# 参考：https://zenn.dev/m193h/articles/20211030sat230551m193habc225

from decimal import Decimal

n = int(input())
INF = 10**18

angle_list = []

for _ in range(n):
    x, y = map(Decimal, input().split())
    start = (y-1)/x
    if x > 1:
        end = y/(x-1)
    else:
        end = INF
    angle_list.append((end, start))

angle_list.sort()

ans = 0
now_angle = 0

for e, s in angle_list:
    if now_angle <= s:
        ans += 1
        now_angle = e

print(ans)
