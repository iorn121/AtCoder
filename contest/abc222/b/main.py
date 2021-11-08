N, P = map(int, input().split())
ans = 0
a = list(map(int, input().split()))
for i in range(N):
    if a[i] < P:
        ans += 1

print(ans)
