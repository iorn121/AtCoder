import sys

input = sys.stdin.readline

N = int(input())
A = input().rstrip()


def f(l, r):
    if l + 1 == r:
        return A[l], 1
    m1 = (2 * l + r) // 3
    m2 = (l + 2 * r) // 3
    val1, cnt1 = f(l, m1)
    val2, cnt2 = f(m1, m2)
    val3, cnt3 = f(m2, r)

    if val1 == val2 == val3:
        return val1, cnt1 + cnt2 + cnt3 - max(cnt1, cnt2, cnt3)
    elif val1 == val2:
        return val1, min(cnt1, cnt2)
    elif val1 == val3:
        return val1, min(cnt1, cnt3)
    elif val2 == val3:
        return val2, min(cnt2, cnt3)


print(f(0, 3**N)[1])
