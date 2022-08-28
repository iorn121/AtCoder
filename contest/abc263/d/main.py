N, L, R = map(int, input().split())
A = list(map(int, input().split()))

Left = [10**9]*(N+1)
Left[0] = 0
for i in range(N):
    Left[i+1] = min(Left[i]+A[i], L*(i+1))

Right = [10**9]*(N+1)
Right[N] = 0
for i in range(N-1, -1, -1):
    Right[i] = min(Right[i+1]+A[i], R*(N-i))

ans = Left[N]+Right[N]
for i in range(N):
    ans = min(ans, Left[i]+Right[i])
print(ans)
