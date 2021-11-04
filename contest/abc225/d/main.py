# 解説：https://qiita.com/u2dayo/items/bf500b82edac4441d9f3

n, q = map(int, input().split())

_next = [-1]*(n+1)
_prev = [-1]*(n+1)

for i in range(q):
    query = list(map(int, input().split()))
    instructions = query[0]

    if instructions == 1:
        x, y = query[1:]
        _next[x] = y
        _prev[y] = x

    if instructions == 2:
        x, y = query[1:]
        _next[x] = -1
        _prev[y] = -1

    if instructions == 3:
        x = query[1]

        ans = []

        current = x
        while _prev[current] != -1:
            current = _prev[current]

        while current != -1:
            ans.append(current)
            current = _next[current]

        print(len(ans), *ans)
