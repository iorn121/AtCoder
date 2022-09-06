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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Alist = []
Blist = []
for i in range(N):
    As = set(A[:i+1])
    Bs = set(B[:i+1])
    Alist.append(As)
    Blist.append(Bs)
Q = int(input())
# print(Alist)
# print(Blist)
for _ in range(Q):
    X, Y = map(lambda x: int(x)-1, input().split())
    print("Yes" if Alist[X] == Blist[Y] else "No")
