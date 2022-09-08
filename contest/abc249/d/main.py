from collections import defaultdict


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


MAX = 2*10**5

c = [0]*(MAX+1)
d = defaultdict(int)
N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    c[a] += 1

for j in range(1, MAX+1):
    k = 1
    while j*k <= MAX:
        i = j*k
        ans += c[i]*c[j]*c[k]
        k += 1
print(ans)
