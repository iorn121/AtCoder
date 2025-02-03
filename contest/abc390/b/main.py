N=int(input())
A = list(map(int, input().split()))

if N==2:
    print("Yes")
else:
    for a0, a1, a2 in zip(A, A[1:], A[2:]):
        if a0*a2!=a1**2:
            print("No")
            exit()
    print("Yes")