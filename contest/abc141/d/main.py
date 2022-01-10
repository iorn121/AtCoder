import heapq


N, M = map(int, input().split())

A = list(map(lambda x: int(x)*(-1), input().split()))

heapq.heapify(A)

for i in range(M):
    max_val = heapq.heappop(A)
    heapq.heappush(A, (-1)*(-max_val//2))

print(-sum(A))
