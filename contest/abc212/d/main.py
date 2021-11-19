import heapq


Q = int(input())
bag = []
heapq.heapify(bag)
now = 0
for _ in range(Q):
    P = list(map(int, input().split()))
    if P[0] == 1:
        heapq.heappush(bag, P[1]-now)
    if P[0] == 2:
        now += P[1]
    if P[0] == 3:
        print(heapq.heappop(bag)+now)
    # print(bag)
