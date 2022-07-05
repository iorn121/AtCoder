N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = sum([abs(A[i]-B[i]) for i in range(N)])
print(ans)
