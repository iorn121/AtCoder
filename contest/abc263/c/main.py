N,M = map(int, input().split())

import itertools

all=itertools.combinations(range(1,M+1),N)

for x in all:
    print(*list(x))