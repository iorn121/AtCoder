import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))
h = []
for q in P:
    heapq.heappush(h, q)
    l = len(h)
    if l > K:
        heapq.heappop(h)
    if l >= K:
        print(h[0])
