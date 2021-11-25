from collections import defaultdict
N, K = map(int, input().split())
C = list(map(int, input().split()))

candyDict = defaultdict(int)
ans = 0

for i in range(N):
    new = C[i]
    candyDict[new] += 1
    if i >= K:
        old = C[i-K]
        candyDict[old] -= 1
        if candyDict[old] == 0:
            del candyDict[old]
    ans = max(ans, len(candyDict))

print(ans)
