N = int(input())
ans = 10**10
for i in range(N):
    A, P, X = map(int, input().split())
    if X-A > 0:
        ans = min(ans, P)
print(ans if ans != 10**10 else -1)
