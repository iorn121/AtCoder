import itertools
from decimal import Decimal
import math

N = int(input())
town = [tuple(map(Decimal, input().split())) for _ in range(N)]
total = 0
for x in itertools.permutations(range(N)):
    for s, t in zip(x[:-1], x[1:]):
        xs, ys = town[s]
        xt, yt = town[t]
        total += math.sqrt((xs-xt)**2+(ys-yt)**2)
total /= math.factorial(N)
print(total)
