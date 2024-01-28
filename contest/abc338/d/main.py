N, M = map(int, input().split())
X = [int(x) - 1 for x in input().split()]
L = [0] * (2 * N + 1)
for s, t in zip(X, X[1:]):
    if s > t:
        t += N
    d = t - s
    L[s] += N - d
    L[t] -= N - d
    L[t] += d
    L[s + N] -= d
# print(L)
for i in range(1, 2 * N + 1):
    L[i] += L[i-1]
# print(L)
ans = 10**18
for i in range(N):
    ans = min(ans,L[i]+L[i+N])
print(ans)
