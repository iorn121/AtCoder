N, K, A = map(int, input().split())

ans = A+K-1
ans %= N
if ans == 0:
    ans = N

print(ans)
