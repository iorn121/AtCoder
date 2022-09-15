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


N = int(input())
named = defaultdict(int)

name = [tuple(input().split()) for _ in range(N)]
for s, t in name:
    named[s] += 1
    named[t] += 1
flg = True
for s, t in name:
    if named[t] > 1 and named[s] > 1:
        if named[s] == 2 and s == t:
            continue
        flg = False
print("Yes" if flg else "No")
