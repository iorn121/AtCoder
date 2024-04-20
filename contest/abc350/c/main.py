N = int(input())
A = [0] + list(map(int, input().split()))
index = {a: i for i, a in enumerate(A)}

ans = []
for i in range(1, N+1):
    while A[i] != i:
        j = index[i]
        A[i], A[j] = A[j], A[i]
        index[A[j]], index[A[i]] = index[A[i]], index[A[j]]
        ans.append((i, j))

print(len(ans))
for a, b in ans:
    print(a, b)