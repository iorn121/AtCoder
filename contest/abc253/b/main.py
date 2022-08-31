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
S = [input() for _ in range(H)]

h = []
w = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            h.append(i)
            w.append(j)

print(abs(h[1]-h[0])+abs(w[1]-w[0]))
