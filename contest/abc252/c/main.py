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
S = [list(input()) for _ in range(N)]

seconds = [[0]*10 for _ in range(10)]
for i in range(N):
    for j, x in enumerate(S[i]):
        seconds[int(x)][j] += 1

ans = [0]*10
for i in range(10):
    for j in range(10):
        ans[i] = max(ans[i], (seconds[i][j]-1)*10+j)

print(min(ans))
