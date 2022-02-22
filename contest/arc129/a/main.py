N, L, R = map(int, input().split())

ans = 0
R += 1

for i in range(61):
    if N >> i & 1:
        l = max(1 << i, L)
        r = min(1 << i+1, R)
        ans += max(0, r-l)

print(ans)
