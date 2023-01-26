import collections
N, Q = map(int, input().split())
X = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(N-1)]
VK = [tuple(map(int, input().split())) for _ in range(Q)]
K_max = 20


class Node:
    def __init__(self, num, X):
        self.children = collections.defaultdict(list)
        self.depth = [-1]*num
        self.parent = [-1]*num
        self.order = []
        self.ans = [[X[i]] for i in range(num)]

    def union(self, x, y):
        self.children[x].append(y)
        self.children[y].append(x)

    def bfs(self, i):
        self.depth[i] = 0
        Q = collections.deque([i])
        while Q:
            q = Q.popleft()
            self.order.append(q)
            for c in self.children[q]:
                if self.depth[c] == -1:
                    self.parent[c] = q
                    self.depth[c] = self.depth[q]+1
                    Q.append(c)

    def operate(self, K_max):
        for i in self.order[1:][::-1]:
            p = self.parent[i]
            # print(i, p)
            self.ans[p].extend(self.ans[i])
            if len(self.ans[p]) > K_max:
                self.ans[p] = sorted(self.ans[p])[-K_max:]
            else:
                self.ans[p].sort()


Tree = Node(N, X)

num_list = [[i] for i in range(N)]
for (A, B) in AB:
    Tree.union(A-1, B-1)
Tree.bfs(0)
Tree.operate(K_max)
# print(Tree.children)
# print(Tree.depth)
# print(Tree.ans)
for V, K in VK:
    print(Tree.ans[V-1][-K])
