from numpy import diff


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = sum([abs(A[i]-B[i]) for i in range(N)])
print("Yes" if K-diff >= 0 and (K-diff) % 2 == 0 else "No")
