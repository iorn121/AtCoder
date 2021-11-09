N = int(input())
A = list(map(int, input().split()))
total = sum(A)
X = int(input())

ans = X//total*N
X -= (X//total)*total
for i in range(N):
    X -= A[i]
    ans += 1
    if X < 0:
        print(ans)
        break
