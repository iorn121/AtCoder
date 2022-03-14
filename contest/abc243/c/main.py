def Yes():
    print("Yes")
    exit(0)


N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
S = input()

right_min, left_max = dict(), dict()

for i in range(N):
    if S[i] == 'R':
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            Yes()
    else:
        if Y[i] in right_min and right_min[Y[i]] < X[i]:
            Yes()

    if S[i] == 'R':
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        else:
            right_min[Y[i]] = X[i]
    else:
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]

print("No")
