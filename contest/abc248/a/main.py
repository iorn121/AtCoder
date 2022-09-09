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


d = defaultdict(int)
S = input()
for s in S:
    n = int(s)
    d[n] += 1
for i in range(10):
    if i not in d:
        print(i)
