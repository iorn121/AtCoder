N, K = map(int, input().split())
if K == 1:
    exit(print(N-1))
prime_count = [0]*(N+1)
is_prime = [True]*(N+1)

for i in range(2, N+1):
    if not is_prime[i]:
        continue
    for j in range(i, N+1, i):
        prime_count[j] += 1
        is_prime[j] = False

ans = 0
for i in prime_count:
    if i >= K:
        ans += 1

print(ans)
