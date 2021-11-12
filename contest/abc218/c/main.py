N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S_cnt = sum(1 for i in range(N) for j in range(N) if S[i][j] == "#")
T_cnt = sum(1 for i in range(N) for j in range(N) if T[i][j] == "#")

if S_cnt != T_cnt:
    print("No")
    exit()


def rotate(S):
    return list(zip(*S[::-1]))


def find_left_top(S):
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                return i, j


def is_same(S, T):
    Si, Sj = find_left_top(S)
    Ti, Tj = find_left_top(T)
    offset_i = Ti-Si
    offset_j = Tj-Sj

    for i in range(N):
        for j in range(N):
            newi = i+offset_i
            newj = j+offset_j
            if 0 <= newi < N and 0 <= newj < N:
                if S[i][j] != T[newi][newj]:
                    return False
            else:
                if S[i][j] == "#":
                    return False
    return True


for _ in range(4):
    if is_same(S, T):
        print("Yes")
        exit()
    S = rotate(S)
print("No")
