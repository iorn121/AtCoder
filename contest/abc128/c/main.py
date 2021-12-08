import itertools
N, M = map(int, input().split())
S = [tuple(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0

for X in itertools.product((True, False), repeat=N):
    cnt = [0]*M
    for i in range(M):
        for s in S[i][1:]:
            if X[s-1]:
                cnt[i] += 1
    total = 0
    for i, c in enumerate(cnt):
        if c % 2 == P[i]:
            total += 1
    if total == M:
        ans += 1


print(ans)
