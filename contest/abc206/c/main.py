from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
    d[A[i]] += 1

ans = N*(N-1)//2

for x, cnt in d.items():
    ans -= cnt*(cnt-1)//2

print(ans)
