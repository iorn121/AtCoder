from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(2):
    A[i] -= 1
    B[i] -= 1
S = [input() for i in range(N)]
check = [[-1]*N for i in range(N)]
dxy = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
que = deque()
que.append(A)
check[A[1]][A[0]] = 0
while que:
    cx, cy = que.pop()
    cp = check[cy][cx]
    for i in range(4):
        for j in range(1, N):
            nx = cx+dxy[i][0]*j
            ny = cy+dxy[i][1]*j
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            if check[ny][nx] != -1:
                continue
            if S[nx][ny] == '#':
                break
            check[ny][nx] = cp+1
            que.append([nx, ny])
print(check[B[1]][B[0]])
