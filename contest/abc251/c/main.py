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
s = set()
tmp = -1
ans = -1
for i in range(N):
    ST = list(input().split())
    S = ST[0]
    T = int(ST[1])
    if S not in s and tmp < T:
        ans = i+1
        tmp = T
    s.add(S)
print(ans)
