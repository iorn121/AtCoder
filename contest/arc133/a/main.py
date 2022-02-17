N = int(input())
A = list(map(int, input().split()))

x = A[-1]
for i in range(N-1):
    if A[i] > A[i+1]:
        x = A[i]
        break

ans = [y for y in A if y != x]
print(*ans)
