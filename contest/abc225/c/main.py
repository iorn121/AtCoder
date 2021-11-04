n, m = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(n)]

check = True
base = B[0][0]

for i in range(n):
    for j in range(m):
        if B[i][j] != base+7*i+j:
            check = False
        if B[i][j] % 7 == 0 and j != m-1:
            check = False

print("Yes" if check else "No")
