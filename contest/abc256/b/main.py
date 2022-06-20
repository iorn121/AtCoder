from collections import Counter
N = int(input())
A = list(map(int, input().split()))

l = []
for i in range(N):
    l.append(0)
    for j in range(i+1):
        l[j] += A[i]

print(sum([1 if i >= 4 else 0 for i in l]))
