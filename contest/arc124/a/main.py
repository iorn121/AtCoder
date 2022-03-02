N, K = map(int, input().split())
MOD = 998244353
fixed = [False]*N
count = [0]*N
for i in range(K):
    c, k = input().split()
    k = int(k)
    k -= 1
    fixed[k] = True
    for j in range(N):
        if c == 'L' and k < j:
            count[j] += 1
        if c == 'R' and j < k:
            count[j] += 1

ans = 1
for i in range(N):
    if fixed[i]:
        continue
    ans = ans*count[i] % MOD
print(ans)
