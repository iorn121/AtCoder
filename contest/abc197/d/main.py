from decimal import Decimal
import math

N = int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())
cx, cy = (x0+xn2)/2, (y0+yn2)/2
x0 -= cx
y0 -= cy

x = cx+x0*math.cos(2*math.pi/N)-y0*math.sin(2*math.pi/N)
y = cy+y0*math.cos(2*math.pi/N)+x0*math.sin(2*math.pi/N)
print(x, y)
