N = int(input())
S = list(input())

X = [ord(S[i])-ord('a') for i in range(N)]
C = [[-1]*(N+1) for i in range(26)]

for i in range(N):
    for j in range(26):
        C[j][i+1] = C[j][i]
    C[X[i]][i+1] = i
R = N

for L in range(N):
    for k in range(X[L]):
        if L < C[k][R]:
            R = C[k][R]
            S[L], S[R] = S[R], S[L]
            break
print(''.join(S))
