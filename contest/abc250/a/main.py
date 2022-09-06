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


H, W = map(int, input().split())
R, C = map(lambda x: int(x)-1, input().split())

cnt = 0
for i in range(H):
    for j in range(W):
        if abs(i-R)+abs(j-C) == 1:
            cnt += 1
            # print(i, j)

print(cnt)
