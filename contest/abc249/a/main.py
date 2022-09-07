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


A, B, C, D, E, F, X = list(map(int, input().split()))

taka = (X//(A+C)*A+min(A, X % (A+C)))*B
aoki = (X//(D+F)*D+min(D, X % (D+F)))*E

if taka == aoki:
    print("Draw")
elif taka > aoki:
    print("Takahashi")
else:
    print("Aoki")
