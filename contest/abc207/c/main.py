N = int(input())


def compare(l1, r1, l2, r2):
    if l1 > l2:
        l1, r1, l2, r2 = l2, r2, l1, r1
    if l2 <= r1:
        return True
    else:
        return False


coodinate = []
for i in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        coodinate.append((2*l, 2*r))
    elif t == 2:
        coodinate.append((2*l, 2*r-1))
    elif t == 3:
        coodinate.append((2*l+1, 2*r))
    else:
        coodinate.append((2*l+1, 2*r-1))
ans = 0
for i in range(N-1):
    l1, r1 = coodinate[i]
    for j in range(i+1, N):
        l2, r2 = coodinate[j]
        ans += compare(l1, r1, l2, r2)

print(ans)
