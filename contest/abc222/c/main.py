N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
rank = [[0, i] for i in range(2*N)]


def judge(a, b):
    if a == b:
        return -1
    if a == 'G' and b == 'P':
        return 1
    if a == 'P' and b == 'C':
        return 1
    if a == 'C' and b == 'G':
        return 1
    return 0


for i in range(M):
    for j in range(N):
        p1 = rank[2*j][1]
        p2 = rank[2*j+1][1]
        result = judge(A[p1][i], A[p2][i])
        if result != -1:
            rank[2*j+result][0] -= 1
    rank.sort()

for _, i in rank:
    print(i+1)
