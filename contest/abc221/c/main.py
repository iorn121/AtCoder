from itertools import permutations

S = sorted(input())[::-1]
A = S[0::2]
B = S[1::2]

for i in range(min(len(A), len(B))):
    if A[i] != B[i]:
        A[i], B[i] = B[i], A[i]
        break

print(int("".join(A))*int("".join(B)))
