X = input()

ans = "Strong"

if X[0] == X[1] == X[2] == X[3]:
    ans = "Weak"


def convert(m, n):
    m = int(m)
    if m+n > 9:
        return m+n-10
    else:
        return m+n


if convert(X[0], 3) == convert(X[1], 2) == convert(X[2], 1) == convert(X[3], 0):
    ans = "Weak"

print(ans)
