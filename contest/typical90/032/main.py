import itertools
N = int(input())
A = [list(map(int, input().split()))for _ in range(N)]

M = int(input())
OK = [[True]*N for _ in range(N)]
for i in range(N):
    OK[i][i] = False
for i in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    OK[X][Y] = False
    OK[Y][X] = False

ans = 10**5
for J in itertools.permutations(range(N)):
    temp = 0
    for i in range(N):
        if i > 0 and (OK[J[i-1]][J[i]] == False):
            # print(J[i-1], J[i], "NG")
            break
        temp += A[J[i]][i]
    else:
        # print("OK", temp)
        ans = min(ans, temp)
        continue
    continue

print(ans if ans != 10**5 else -1)
