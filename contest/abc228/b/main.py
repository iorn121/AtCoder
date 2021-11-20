N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
seen = [False]*(N+1)
now = X
while not seen[now]:
    # print(now, A[now-1])
    ans += 1
    seen[now] = True
    now = A[now-1]
print(ans)
