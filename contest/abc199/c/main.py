N = int(input())
S = list(input())
Q = int(input())

flg = 0


def convert(x):
    if x < N:
        x += N
    else:
        x -= N
    return x


for i in range(Q):
    T, A, B = map(int, input().split())
    A -= 1
    B -= 1
    if T == 1:
        if flg % 2 != 0:
            A = convert(A)
            B = convert(B)
        S[A], S[B] = S[B], S[A]
    else:
        flg += 1

if flg % 2 != 0:
    S = S[N:]+S[:N]
print("".join(S))
