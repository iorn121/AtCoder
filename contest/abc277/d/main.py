from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

T = []
total = x = A[0]
for a in A[1:]:
    if a-x not in (0, 1):
        T.append(total)
        total = 0
    total += a
    x = a

if len(T) and (A[-1]+1) % M == A[0]:
    T[0] += total
else:
    T.append(total)
print(sum(A)-max(T))
