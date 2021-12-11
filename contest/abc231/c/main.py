N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for i in range(Q):
    X = int(input())
    left = -1
    right = N
    while right-left > 1:
        mid = (left+right)//2
        if A[mid] < X:
            left = mid
        else:
            right = mid
    print(N-right)
