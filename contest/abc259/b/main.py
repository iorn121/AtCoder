import math
a, b, d = map(float, input().split())


d = math.radians(d)
x = complex(a, b)
y = complex(math.cos(d), math.sin(d))

z = x*y
print(f"{z.real:.7f} {z.imag:.7f}")
