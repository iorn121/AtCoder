import math
P = float(input())


def f(x):
    return x+P*2**-(x/1.5)


def bibun(x):
    return 1-(2*P/3) * pow(1/2, (2*x)/3) * math.log(2)


l = 0
r = 10**10

while r-l > 0.000001:
    mid = (l+r)/2
    a = bibun(mid)
    if a > 0:
        r = mid
    else:
        l = mid

print(f(l))
