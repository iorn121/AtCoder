from re import M


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


N, A, B = map(int, input().split())

for i in range(N):
    S = []
    for j in range(N):
        if (i+j) % 2 == 0:
            S.append(B*".")
        else:
            S.append(B*"#")
    for k in range(A):
        print("".join(S))
