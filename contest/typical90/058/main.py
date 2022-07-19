N, K = map(int, input().split())
visited = [-1]*(10**5)
loop_start = 0
loop_cycle = 10**5
loop = [N]
visited[N] = 0
for i in range(1, K+1):
    x = sum(list(map(int, str(N))))
    N = (N+x) % (10**5)
    if visited[N] == -1:
        visited[N] = i
        loop.append(N)
    else:
        loop_cycle = visited[N]-i
        loop_start = visited[N]
        loop = loop[loop_start:]
        # print(loop_start, loop_cycle, loop)
        break
    # print(N, loop)
print(loop[(K-loop_start) % loop_cycle])
