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


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

eat_max = max(A)
eat_set = set()
for i, a in enumerate(A, 1):
    if a == eat_max:
        eat_set.add(i)

eat_flg = False
for k in B:
    if k in eat_set:
        eat_flg = True

print("Yes" if eat_flg else "No")
