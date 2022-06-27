N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
check = [False]*(N+1)
for a in A:
    check[a] = True
for q in L:
    q -= 1
    if A[q] == N:
        continue
    if check[A[q]+1]:
        continue
    check[A[q]] = False
    check[A[q]+1] = True
    A[q] += 1

print(*A)
