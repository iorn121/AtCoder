N, Q = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
X_Y_MAX = -10**9
X_Y_MIN = 10**9
Y_X_MAX = -10**9
Y_X_MIN = 10**9
for i, (x, y) in enumerate(P):
    X_Y_MAX = max(X_Y_MAX, x+y)
    X_Y_MIN = min(X_Y_MIN, x+y)
    Y_X_MAX = max(Y_X_MAX, x-y)
    Y_X_MIN = min(Y_X_MIN, x-y)
for _ in range(Q):
    q = int(input())
    q -= 1
    ans = 0
    ans = max(ans, X_Y_MAX-sum(P[q]))
    ans = max(ans, sum(P[q])-X_Y_MIN)
    ans = max(ans, Y_X_MAX-(P[q][0]-P[q][1]))
    ans = max(ans, (P[q][0]-P[q][1])-Y_X_MIN)
    print(ans)
