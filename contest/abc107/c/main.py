N, K = map(int, input().split())
X = list(map(int, input().split()))
ans = 10**10
for i in range(N-K+1):
    if X[i] < 0 and X[i+K-1] > 0:
        l = max(abs(X[i]), X[i+K-1])
        s = min(abs(X[i]), X[i+K-1])
        ans = min(l+s*2, ans)
    elif X[i] < 0:
        ans = min(abs(X[i]), ans)
    else:
        ans = min(abs(X[i+K-1]), ans)
print(ans)
