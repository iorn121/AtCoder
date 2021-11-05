from decimal import Decimal

N = int(input())

A, B, time = [], [], []
ans = 0
total = 0

for i in range(N):
    a, b = map(Decimal, input().split())
    A.append(a)
    B.append(b)
    t = a/b
    total += t
    time.append(t)

rem = total/2

for i, x in enumerate(time):
    if x <= rem:
        ans += A[i]
        rem -= x
    else:
        ans += B[i]*rem
        break

print(ans)
