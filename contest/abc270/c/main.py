from collections import deque
import sys


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


N, X, Y = map(int, input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for i in range(N-1):
    U, V = map(lambda x: int(x)-1, input().split())
    G[U].append(V)
    G[V].append(U)
sys.setrecursionlimit(10**6)
stack = deque()
stack.append(X)
par = [-1]*N
par[X] = X
while stack:
    c = stack.popleft()
    for nex in G[c]:
        if par[nex] == -1:
            par[nex] = c
            stack.append(nex)
ans = []
# print(par)
while Y != par[Y]:
    ans.append(Y+1)
    Y = par[Y]
ans.append(X+1)
print(*ans[::-1])
