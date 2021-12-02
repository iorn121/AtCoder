N = int(input())

check = [False]*N

A = list(map(int, input().split()))

for i in range(N):
    check[A[i]-1] = True

print("No" if False in check else "Yes")
