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


N, Q = map(int, input().split())
num = [i for i in range(N)]
table = [i+1 for i in range(N)]
for q in range(Q):
    x = int(input())
    now = num[x-1]
    nex = now+1 if now < N-1 else now-1
    y = table[nex]
    # print(x, y, now, nex)
    num[x-1] = nex
    num[y-1] = now
    table[now], table[nex] = y, x
    # print("---")
    # print(*num)
    # print(*table)
print(*table)
