import math
R, X, Y = map(int, input().split())

distance = math.sqrt(X**2+Y**2)

if distance < R:
    print(2)
else:
    print(math.ceil(distance/R))
