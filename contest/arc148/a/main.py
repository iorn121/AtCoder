import math


def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


N = int(input())
A = list(map(int, input().split()))
A.sort()
g = 0
for i in range(N-1):
    g = math.gcd(g, A[i+1]-A[i])

print(2 if g == 1 else 1)
