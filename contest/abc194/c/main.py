N = int(input())
A = list(map(int, input().split()))
s = sum(A)
ans = 0
for i in range(N):
    ans += A[i]**2*(N-1)
    ans -= A[i]*(s-A[i])
print(ans)
