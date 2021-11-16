from itertools import permutations

S, K = input().split()
K = int(K)
S_set = set(["".join(p) for p in permutations(S)])
S_list = list(S_set)
S_list.sort()
print(S_list[K-1])
