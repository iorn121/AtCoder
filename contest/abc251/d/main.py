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


W = int(input())

ans = []
for i in range(1, 100):
    ans.append(i)
    ans.append(i*100)
    ans.append(i*10000)
print(len(ans))
print(*ans)
