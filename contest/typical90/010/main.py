import pprint
N = int(input())
PQ = [[0]*2 for _ in range(N+1)]
for i in range(N):
    C, P = map(int, input().split())
    C -= 1
    PQ[i+1][:] = PQ[i][:]
    PQ[i+1][C] += P
Q = int(input())
# pprint.pprint(PQ)
for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    print(f"{PQ[R][0]-PQ[L][0]} {PQ[R][1]-PQ[L][1]}")
