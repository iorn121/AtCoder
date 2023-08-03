def f(X):
    p = X[0]
    X = X[1:]
    l = len(X)
    if l == 0:
        return (int(p)+1)//5
    if p == "0":
        return f(X)
    pp = str(int(p)-1)
    ret = f(pp)*10**l + (int(pp)-f(pp)+1)*(10**l-8**l)
    if p in "49":
        return ret + int(X) + 1
    else:
        return ret + f(X)


A, B = input().split()
A = str(int(A)-1)


print(f(B)-f(A))
