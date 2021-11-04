h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

judge = True

for row2 in range(h):
    for row1 in range(row2):
        for col2 in range(w):
            for col1 in range(col2):
                if a[row1][col1]+a[row2][col2] > a[row2][col1]+a[row1][col2]:
                    judge = False

print("Yes" if judge == True else "No")
