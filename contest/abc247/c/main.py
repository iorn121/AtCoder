from functools import lru_cache


N = int(input())


@lru_cache(maxsize=None)
def S(x: int):
    if x == 1:
        return [1]
    return S(x-1)+[x]+S(x-1)


print(*S(N))
