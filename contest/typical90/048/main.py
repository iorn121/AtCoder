import heapq
N, K = map(int, input().split())

AB = [tuple(map(int, input().split())) for i in range(N)]


can_solve = [(AB[i][1]*(-1), (AB[i][0]-AB[i][1])*(-1)) for i in range(N)]
ans = 0
heapq.heapify(can_solve)
for i in range(K):
    solve_it, next_solve = heapq.heappop(can_solve)
    # print(solve_it, next_solve)
    ans += solve_it*(-1)
    heapq.heappush(can_solve, (next_solve, 0))

print(ans)
