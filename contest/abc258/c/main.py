N, Q = map(int, input().split())
S = input()
x=0
for _ in range(Q):
    n, xx = map(int, input().split())
    if n == 1:
        x+=xx
        x%=N
    else:
        print(S[xx-1-x])
