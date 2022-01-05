from itertools import product
N, X = map(int, input().split())

ans = 0
a = []
for i in range(N):
    x = list(map(int, input().split()))
    a.append(x[1:])

for nums in product(*a):
    cnt = 1
    for x in nums:
        cnt *= x

    if cnt == X:
        ans += 1

print(ans)
