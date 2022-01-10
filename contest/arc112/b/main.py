B, C = map(int, input().split())


def f(b, c):
    if c == 0:
        return b, b
    elif c % 2 == 0:
        return b-c//2, b+c//2-1
    else:
        return -b-c//2, -b+c//2


x1, y1 = f(B, C)
x2, y2 = f(B, C-1)

print(y1-x1+1+y2-x2+1-max(0, min(y1, y2)-max(x1, x2)+1))
