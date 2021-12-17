N, A, B, C = map(int, input().split())
l = []
INF = 10**18
for i in range(N):
    l.append(int(input()))


def dfs(i, a, b, c):
    if i == N:
        if a == 0 or b == 0 or c == 0:
            return INF
        return abs(a-A)+abs(b-B)+abs(c-C)

    res = dfs(i+1, a, b, c)

    res = min(res, dfs(i+1, a+l[i], b, c)+(10 if a else 0))
    res = min(res, dfs(i+1, a, b+l[i], c)+(10 if b else 0))
    res = min(res, dfs(i+1, a, b, c+l[i])+(10 if c else 0))

    return res


print(dfs(0, 0, 0, 0))
