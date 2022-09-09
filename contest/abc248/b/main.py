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


A, B, K = map(int, input().split())

cnt = 0
while A*(K**cnt) < B:
    cnt += 1
print(cnt)
