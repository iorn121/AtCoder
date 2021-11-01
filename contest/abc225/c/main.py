n, m = map(int, input().split())

B = [[int(x) for x in input().split()] for _ in range(n)]

check_rows = [1]*n

for i in range(n):
    for j in range(m-1):
        if B[i][j]+1 != B[i][j+1]:
            check_rows[i] = 0
    if i > 0:
        if B[i-1][0]+7 != B[i][0]:
            check_rows[i] = 0

print("No" if 0 in check_rows else "Yes")
