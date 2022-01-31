N = int(input())
aisyou = [[-1]*(N*2) for i in range(N*2)]

for i in range(N):
    A = list(map(int, input().split()))
    for j, a in enumerate(A):
        aisyou[i][j+1] = a
