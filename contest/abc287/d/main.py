import re
from array import array
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LII(H): return [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
def S(): return sys.stdin.readline().rstrip()
def SS(H): return [S() for _ in range(H)]
def LS(): return list(sys.stdin.readline().rstrip().split())
def ARRAY(L): return array("i", L)


MOD = 998244353

# 累積和 ans=list(itertools.accumulate(L))
# 順列 ans=list(itertools.permutation(L))
# 重複なし組み合わせ ans=list(itertools.combinations(L,2))
# 重複あり組み合わせ ans=list(itertools.combinations_with_replacement(L,2))
# nCr ans=math.comb(n,r)


# Nまでの数を素数かどうか判定（エラトステネスのふるい）
def prime_list(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime


# 素因数分解
def prime_factorization(N: int):
    arr = []
    sqrt = int(math.sqrt(N))
    for i in range(2, sqrt+1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                cnt += 1
                N //= i
            arr.append([i, cnt])
    if N != 1:
        arr.append([N, 1])
    return arr


# 1文字ずつ文字列をずらしたときの最長共通接頭辞の長さ
def z_algorithm(S: string):
    n = len(S)
    rtn = [-1]*n
    rtn[0] = n
    i, j = 1, 0
    while i < len(S):
        while i+j < len(S) and S[j] == S[i+j]:
            j += 1
        rtn[i] = j
        if j == 0:
            i += 1
        k = 1
        while i+k < len(S) and k+rtn[k] < j:
            rtn[i+k] = rtn[k]
            k += 1
        i += k
        j -= k
    return rtn


# Nまでの積をxで何回割り切れるか
def divide_num(N: int, x: int):
    rtn = 0
    i = 1
    while pow(x, i) <= N:
        rtn += N//pow(x, i)
        i += 1
    return rtn


# 拡張ユークリッド互除法
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a//b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0


# 逆元を求める
def modinv(a, mod=MOD):
    g, x, y = xgcd(a, mod)
    if g != 1:
        raise Exception("moduler inverse does not exist")
    else:
        return x % mod


class BIT:
    # 長さN+1の配列を初期化
    def __init__(self, N):
        self.size = N
        self.bit = [0]*(N+1)

    # i番目までの和を求める
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]  # フェニック木のi番目の値を加算
            i -= -i & i  # 最も右にある1の桁を0にする
        return res

    # i番目の値にxを足して更新する
    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x  # フェニック木のi番目にxを足して更新
            i += -i & i  # 最も右にある1の桁に1を足す


# N mod p = a, N mod q = b
# px + a = qy + b
# px - qy = b-a
# px = 1 mod q
def crp(a, p, b, q):
    x = pow(p, -1, q)
    x *= b-a
    x %= q
    return p*x + a


def Dijkstra(edges, num_node):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node  # スタート地点以外の値は∞で初期化
    node[0] = 0  # スタートは0で初期化

    node_name = [i for i in range(num_node)]  # ノードの名前を0~ノードの数で表す

    while len(node_name) > 0:
        r = node_name[0]

        # 最もコストが小さい頂点を探す
        for i in node_name:
            if node[i] < node[r]:
                r = i  # コストが小さい頂点が見つかると更新

        # 最もコストが小さい頂点を取り出す
        min_point = node_name.pop(node_name.index(r))

        # 経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]  # 終点
            cost = factor[1]  # コスト

            # 更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost  # 更新

    return node


def EulerTour(n, graph, root):
    """
    (n: int, graph: List[List[int]], root: int) -> Tuple[List[int], List[int], List[int]]:

    :param n: the number of vertex points
    :param graph: 2D matrix of N vertices given by the edges
    :param root: start node index

    :return tour: order of visited vertex
    :return in_time: first visiting time of each vertex
    :return out_time: last visiting time of each vertex

    example:
    graph = [[] for _ in range(n)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tour, in_time, out_time = EulerTour(n, graph, 0)
    """

    parent = [-1] * n
    stack = [~root, root]  # postorder, preorder
    curr_time = -1
    tour = []
    in_time = [-1] * n
    out_time = [-1] * n
    while stack:
        curr_node = stack.pop()
        curr_time += 1
        if curr_node >= 0:  # preorder
            tour.append(curr_node)
            if in_time[curr_node] == -1:
                in_time[curr_node] = curr_time

            for next_node in graph[curr_node]:
                if next_node != parent[curr_node]:
                    parent[next_node] = curr_node
                    stack.append(~next_node)
                    stack.append(next_node)
        elif curr_node < 0:  # postorder
            out_time[~curr_node] = curr_time
            if parent[~curr_node] != -1:
                tour.append(parent[~curr_node])

    return tour, in_time, out_time


s = S()
t = S()
N = len(s)
M = len(t)
f_s = s[:M]
b_s = s[-M:]

f_s_check = [True]

b_s_check = [True]
for x, z in zip(f_s, t):
    if x == z or x == "?" or z == "?":
        f_s_check.append(f_s_check[-1])
    else:
        f_s_check.append(False)
for y, z in zip(b_s[::-1], t[::-1]):
    if y == z or y == "?" or z == "?":
        b_s_check.append(b_s_check[-1])
    else:
        b_s_check.append(False)
b_s_check.reverse()
# print(*f_s_check)
# print(*b_s_check)
for x, y in zip(f_s_check, b_s_check):
    if x and y:
        print("Yes")
    else:
        print("No")
