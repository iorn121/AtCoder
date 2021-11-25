N, A, X, Y = map(int, input().split())

ans = 0
if N > A:
    ans = A*X+(N-A)*Y
else:
    ans = N*X

print(ans)
