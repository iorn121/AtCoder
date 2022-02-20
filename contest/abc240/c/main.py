N, X = map(int, input().split())
dp = 1
for i in range(N):
    a, b = map(int, input().split())
    dp = (dp << a) | (dp << b)
print("Yes" if (dp >> X) & 1 == 1 else "No")
