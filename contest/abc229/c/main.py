N, W = map(int, input().split())
cheese = []
for i in range(N):
    A, B = map(int, input().split())
    cheese.append((A, B))

cheese.sort(reverse=True)

ans = 0

for i in range(N):
    if W > cheese[i][1]:
        ans += cheese[i][0]*cheese[i][1]
        W -= cheese[i][1]
    else:
        ans += cheese[i][0]*W
        break

print(ans)
