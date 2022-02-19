from collections import defaultdict
N, Q = map(int, input().split())
X = list(map(int, input().split()))


class Node:
    def __init__(self, num):
        self.parent = [-1]*num
        self.children = [[i] for i in range(num)]

    def union(self, x, y):
        if x > y:
            x, y = y, x
        if self.parent[y] != -1:
            x, y = y, x
        self.parent[y] = x
        self.children[x].extend(self.children[y])


Tree = Node(N)

num_list = [[i] for i in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    Tree.union(A, B)

print(Tree.children)

for i in range(Q):
    V, K = map(int, input().split())
    V -= 1
    K -= 1
