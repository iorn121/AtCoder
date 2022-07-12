A, B = map(int, input().split())


def euclidean(x, y):
    if y == 0:
        return x
    return euclidean(y, x % y)


ans = A*B//euclidean(A, B)
print(ans if ans <= 10**18 else "Large")
