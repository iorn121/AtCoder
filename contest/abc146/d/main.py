from collections import deque
import sys
sys.setrecursionlimit(10**9)

def dfs(cu, seen, pa=-1, col=0):
    used = set()
    used.add(col)
    seen.add(cu)
    c = 1
    for to in E[cu]:
        if to[0] in seen:
            continue
        # print(cu,to)
        if to[0] != pa:
            while c in used:
                c += 1
            ans[to[1]] = c
            dfs(to[0], seen, cu, c)
            c += 1

def main():
    global N, E, ans
    N = int(input())
    E = [[] for _ in range(101010)]
    ans = [0]*N
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        E[a].append((b, i))
        E[b].append((a, i))
    dfs(0, set())
    # print(ans)
    ma = 0
    for i in range(N):
        ma = max(ma, len(E[i]))
    print(ma)
    for i in range(N - 1):
        print(ans[i])

if __name__ == "__main__":
    main()