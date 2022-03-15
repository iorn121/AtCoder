N, X = map(int, input().split())
S = input()
T = []
for s in S:
    if s == 'U' and len(T) > 0 and (T[-1] == 'R' or T[-1] == 'L'):
        T.pop()
    else:
        T.append(s)
for t in T:
    if t == 'R':
        X = X*2+1
    elif t == 'L':
        X = X*2
    else:
        X = X//2
print(X)
