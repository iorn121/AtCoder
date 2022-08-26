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


X, Y, N = map(int, input().split())


def solve():
    ans = (N//3)*Y+(N % 3)*X
    ans = min(ans, X*N)
    return ans


print(solve())
