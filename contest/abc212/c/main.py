N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
numList = []
append = numList.append
for i in range(N):
    append((A[i], "A"))
for i in range(M):
    append((B[i], "B"))
numList.sort()
ans = 10**10
for i in range(len(numList)-1):
    pre, preX = numList[i]
    nex, nexX = numList[i+1]
    if preX != nexX:
        ans = min(ans, abs(pre-nex))
print(ans)
