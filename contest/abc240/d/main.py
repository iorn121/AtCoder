N = int(input())
A = list(map(int, input().split()))

ans = [0]*N
now = 0
l = []
for i, x in enumerate(A):
    now += 1
    if not l:
        l = [[x, 1]]
    elif l[-1][0] == x:
        l[-1][1] += 1
    else:
        l.append([x, 1])
    while l and l[-1][0] == l[-1][1]:
        y, j = l.pop()
        now -= j
    ans[i] = now
print(*ans)
