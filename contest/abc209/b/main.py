N, X = map(int, input().split())
A = list(map(int, input().split()))

needed = sum(A)-len(A)//2
print("Yes" if needed <= X else "No")
