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


X, Y, Z = map(int, input().split())

if X*Y < 0 or abs(X) < abs(Y):
    exit(print(abs(X)))

if Z < Y < X or X < Y < Z:
    ans = abs(X)
    if X*Z < 0:
        ans += abs(Z)*2
    exit(print(ans))

print(-1)
