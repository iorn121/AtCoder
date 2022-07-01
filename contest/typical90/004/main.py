H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
row = [0]*H
col = [0]*W
for i in range(H):
    row[i] = sum(A[i])
for j in range(W):
    col[j] = sum([A[i][j] for i in range(H)])
for i in range(H):
    ans = [row[i]+col[j]-A[i][j] for j in range(W)]
    print(*ans)
