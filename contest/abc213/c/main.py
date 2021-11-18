H, W, N = map(int, input().split())
row = []
col = []
for i in range(N):
    A, B = map(int, input().split())
    row.append(A)
    col.append(B)
Xconvert = {x: i+1 for i, x in enumerate(sorted(list(set(row))))}
Yconvert = {y: i+1 for i, y in enumerate(sorted(list(set(col))))}

for i in range(N):
    print(Xconvert[row[i]], Yconvert[col[i]])
