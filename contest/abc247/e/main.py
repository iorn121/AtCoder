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


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


def calc(B):
    i, j, cx, cy, res = 0, 0, 0, 0, 0
    l = len(B)
    while i < l:
        while j < l and (cx == 0 or cy == 0):
            if B[j] == X:
                cx += 1
            if B[j] == Y:
                cy += 1
            j += 1
        if cx > 0 and cy > 0:
            res += l-j+1
        if B[i] == X:
            cx -= 1
        if B[i] == Y:
            cy -= 1
        i += 1
    return res


s, ans = 0, 0
while s < N:
    B = []
    while s < N and Y <= A[s] <= X:
        B.append(A[s])
        s += 1
    if len(B) > 0:
        ans += calc(B)
    else:
        s += 1
print(ans)

