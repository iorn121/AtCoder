import math
from decimal import Decimal
T = float(input())
L, X, Y = map(float, input().split())
Q = int(input())
for _ in range(Q):
    E = float(input())
    x = math.sqrt(X**2+(Y+L/2*math.sin(2*E/T*math.pi))**2)
    y = L/2*(1-math.cos(2*E/T*math.pi))
    theta = math.degrees(math.atan2(y, x))
    print(f"{theta:.10g}")
