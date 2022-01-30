H, W = map(int, input().split())

A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)
tans = []
for i in range(W):
    ans = []
    for j in range(H):
        ans.append(A[j][i])
    tans.append(ans)
for i in range(W):
    print(*tans[i])
