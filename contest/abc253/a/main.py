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


X = list(map(int, input().split()))
if (max(X) != X[1]) and (min(X) != X[1]) or len(set(X)) != 3:
    print("Yes")
else:
    print("No")
