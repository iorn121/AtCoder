N = int(input())

login = []
append = login.append
for i in range(N):
    A, B = map(int, input().split())
    append((A, 1))
    append((A+B, -1))

login.sort()

ans = [0]*N
now = 0
today = 0
for x, y in login:
    if now != 0:
        ans[now-1] += x-today
    now += y
    today = x


print(*ans)
