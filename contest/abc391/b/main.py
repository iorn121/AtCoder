N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for i in range(N-M+1):
    for j in range(N-M+1):
        flg = True
        for k in range(M):
            for l in range(M):
                if S[i+k][j+l] != T[k][l]:
                    flg = False
                    break
        if flg:
            print(i+1, j+1)
            exit()