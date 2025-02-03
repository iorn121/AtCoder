import heapq
N, W = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
TA = [list(map(int, input().split())) for _ in range(Q)]

col = [[] for _ in range(W)]
col_num = [0]*W
for i,(x, y) in enumerate(XY):
    x -= 1
    y-= 1
    heapq.heappush(col[x], (y, i))
    col_num[x] += 1

delete_time = [-1 for _ in range(N)]
delete_pre = -1

while min(col_num) > 0:
    time = 0
    block = []
    for i in range(W):
        by, bi = heapq.heappop(col[i])
        time = max(time, by)
        block.append(bi)
        col_num[i] -= 1
    delete_pre = max(delete_pre+1, time)
    for b in block:
        delete_time[b] = delete_pre

# print(delete_time)

for t, a in TA:
    a -= 1
    if delete_time[a] == -1 or delete_time[a] >= t:
        print("Yes")
    else:
        print("No")