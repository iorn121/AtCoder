N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
left = 0
right = 1001
for i in range(N):
    left = max(left, A[i])
    right = min(right, B[i])
if left > right:
    print(0)
else:
    print(right-left+1)
