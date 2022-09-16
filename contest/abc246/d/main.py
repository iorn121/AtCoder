N = int(input())


def f(x, y):
    return x**3+x**2*y+x*y**2+y**3


X = 10**18
a, b = 0, 10**6

while a <= b:
    tmp = f(a, b)
    if tmp >= N:
        X = min(X, tmp)
        b -= 1
    else:
        a += 1

print(X)
