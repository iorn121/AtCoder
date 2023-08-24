import heapq


def divceil(n, k): return 1+(n-1)//k  # n/kの切り上げを返す


def main():
    n, m, x, y = map(int, input().split())

    graph = [[] for _ in range(n)]

    for i in range(m):
        s, t, tm, km = map(int, input().split())
        s -= 1
        t -= 1
        graph[s].append((t, tm, km))
        graph[t].append((s, tm, km))

    mindist = [-1] * n
    hq = []
    heapq.heappush(hq, (0, x-1))
    while hq:
        dist, node = heapq.heappop(hq)
        if mindist[node] != -1:
            continue
        mindist[node] = dist
        for i, t, k in graph[node]:
            if mindist[i] != -1:
                continue
            heapq.heappush(hq, (divceil(dist, k)*k+t, i))

    print(mindist[y-1])


if __name__ == '__main__':
    main()
