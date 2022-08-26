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


N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
ruiseki = [0]*(N+1)
for i in range(N):
    ruiseki[i+1] = ruiseki[i]+A[i]
check = set(ruiseki)
canChoose = False
for i in range(N-2):
    offset = ruiseki[i]
    nP = P+offset
    nQ = nP+Q
    nR = nQ+R
    if nP in check and nQ in check and nR in check:
        canChoose = True

print("Yes" if canChoose else "No")
