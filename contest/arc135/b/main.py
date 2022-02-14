from calendar import c


N = int(input())
S = list(map(int, input().split()))

check = [0, 0]
for s in S:
    check.append(s-check[-1]-check[-2])
c1 = -min(check[::3])
c2 = -min(check[1::3])
c3 = min(check[2::3])
if c1+c2 > c3:
    print("No")
    exit()
add = [c1, c2, -c1-c2]
ans = [x + add[i % 3] for i, x in enumerate(check)]

print("Yes")
print(*ans)
