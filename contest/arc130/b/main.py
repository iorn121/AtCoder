H, W, C, Q = map(int, input().split())
ans = [0]*C
instructions = []
for i in range(Q):
    t, n, c = map(int, input().split())
    n -= 1
    c -= 1
    instructions.append((t, n, c))

row = set()
col = set()
for i in range(Q-1, -1, -1):
    t, n, c = instructions[i]
    if t == 1:
        if n in row:
            continue
        row.add(n)
        ans[c] += W-len(col)
    else:
        if n in col:
            continue
        col.add(n)
        ans[c] += H-len(row)

print(*ans)
