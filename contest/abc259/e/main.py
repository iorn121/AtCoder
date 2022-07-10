from collections import defaultdict
N = int(input())

prime = {}

for i in range(N):
    m = int(input())
    for j in range(m):
        p, e = map(int, input().split())
        if p in prime:
            if e > prime[p][0]:
                prime[p] = (e, i, 1)
            elif e == prime[p][0]:
                prime[p] = (e, prime[p][1], 2)
        else:
            prime[p] = (e, i, 1)
ans = set()
for p in prime:
    # print(prime[p])
    if prime[p][2] > 1:
        continue
    ans.add(prime[p][1])
print(min(N, len(ans)+1))
