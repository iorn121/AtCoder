import math
A, B, W = map(int, input().split())
W *= 1000
lower = math.ceil(W/B)
upper = math.floor(W/A)
if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)
