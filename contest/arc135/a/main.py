from functools import lru_cache

MOD = 998244353


@lru_cache
def f(x):
    if x < 5:
        return x
    x1 = x//2
    x2 = (x+1)//2
    return f(x1)*f(x2) % MOD


X = int(input())
print(f(X))
