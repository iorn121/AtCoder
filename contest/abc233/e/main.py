from itertools import accumulate
S = input()
N = len(S)
ans = 0

A = [*accumulate(map(int, S))]
for i in range(N-1, 0, -1):
    if A[i]//10 == 0:
        continue
    q, mod = divmod(A[i], 10)
    A[i] = mod
    A[i-1] += q
print("".join(map(str, A)))
