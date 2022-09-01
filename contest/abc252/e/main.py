import heapq


def print_func_info(func):
    def wrapper(*args, **kwargs):
        print(f"executing {func}")
        for arg in args:
            print(f":param {type(arg)} {arg}")
        results = func(*args, **kwargs)
        for result in results:
            print(f":return: {result}")
        return results
    return wrapper


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append((B, C, i+1))
    G[B].append((A, C, i+1))


def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [10**15]*N
    cost[0] = 0
    chosen = [-1]*N
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue
        for nv, nc, nr in G[v]:
            tmp = nc+c
            if tmp < cost[nv]:
                cost[nv] = tmp
                chosen[nv] = nr
                heapq.heappush(hq, (tmp, nv))
        # print(cost)
        # print(chosen)
    return chosen


chosen = dijkstra(0)
print(*chosen[1:])
