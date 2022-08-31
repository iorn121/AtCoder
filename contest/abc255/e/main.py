from collections import defaultdict
N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))

A0 = [0]
nex = 0
for i in range(N-1):
    A0.append(S[i]-A0[-1])

d = defaultdict(int)
for i, a in enumerate(A0):
    for x in X:
        diff = x-a
        if i % 2 == 1:
            diff *= -1
        d[diff] += 1

ans = 0
for k, v in d.items():
    ans = max(ans, v)

print(ans)
