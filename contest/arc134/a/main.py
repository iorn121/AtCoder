N, L, W = map(int, input().split())
A = list(map(int, input().split()))

r = 0
ans = 0
A.append(L)
for a in A:
    if r < a:
        ans += (a-r+W-1)//W
    r = a+W

print(ans)
