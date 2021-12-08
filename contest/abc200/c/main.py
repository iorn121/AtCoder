from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

amari = defaultdict(int)

for i in range(N):
    amari[A[i] % 200] += 1

ans = 0
for k, v in amari.items():
    ans += v*(v-1)//2
print(ans)
