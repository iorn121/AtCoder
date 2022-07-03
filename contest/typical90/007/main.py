N = int(input())
A = list(map(int, input().split()))
A.sort()


def nibutan(x):
    l = 0
    r = N
    while l+1 < r:
        mid = (l+r)//2
        if A[mid] > x:
            r = mid
        else:
            l = mid
    return l


# print(A)
Q = int(input())
for _ in range(Q):
    B = int(input())
    x = nibutan(B)
    if x == N-1:
        print(min(abs(B-A[x]), abs(B-A[x-1])))
    else:
        print(min(abs(B-A[x]), abs(B-A[x+1])))
