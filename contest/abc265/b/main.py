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


N, M, T = map(int, input().split())
A = list(map(int, input().split()))
for i in range(M):
    X, Y = map(int, input().split())
    X -= 1
    A[X] -= Y

canMove = True
for i in range(N-1):
    T -= A[i]
    if T <= 0:
        canMove = False

print("Yes" if canMove else "No")
