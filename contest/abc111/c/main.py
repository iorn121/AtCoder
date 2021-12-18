from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

even_d = defaultdict(int)
odd_d = defaultdict(int)
s = set(A)
if len(s) == 1:
    print(N//2)
    exit()

for i in range(N):
    if i % 2 == 0:
        even_d[A[i]] += 1
    else:
        odd_d[A[i]] += 1
even = sorted(even_d.items(), key=lambda v: v[1], reverse=True)
odd = sorted(odd_d.items(), key=lambda v: v[1], reverse=True)
ans = N
if even[0][0] == odd[0][0]:
    ans -= max(even[1][1]+odd[0][1], even[0][1]+odd[1][1])
else:
    ans -= even[0][1]+odd[0][1]
print(ans)
