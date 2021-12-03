import numpy as np

N = int(input())
T = list(map(int, input().split()))
S = np.sum(T)
DP = np.zeros(S//2+1, dtype=np.bool)
DP[0] = 1
for i in range(N):
    if T[i] > S//2+1:
        continue
    DP[T[i]:] |= DP[:S//2+1-T[i]]  # numpyを用いていっぺんに遷移

DP = DP[::-1]

print(S-S//2+np.argmax(DP))
