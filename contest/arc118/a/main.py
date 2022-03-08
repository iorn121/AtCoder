t, N = map(int, input().split())
N -= 1
period = 100+t
check = [False]*(100+t)
for i in range(100):
    x = (100+t)*i//100
    check[x] = True
num = check.count(False)
c = []
for i, n in enumerate(check):
    if not n:
        c.append(i)
ans = c[N % num]+period*(N//num)
print(ans)
