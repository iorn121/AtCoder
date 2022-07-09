import pprint

N = int(input())
M = 1001
imosu = [[0]*M for _ in range(M)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ry-ly):
        imosu[ly+i][lx] += 1
        imosu[ly+i][rx] -= 1

# print(M)


ans = [0]*(N+1)
for i in range(M):
    for j in range(1, M):
        imosu[i][j] += imosu[i][j-1]

for j in range(M):
    for i in range(M):
        ans[imosu[i][j]] += 1
# pprint.pprint(result)
for k in range(1, N+1):
    print(ans[k])
