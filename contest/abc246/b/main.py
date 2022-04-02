from decimal import Decimal
import math
A, B = map(Decimal, input().split())
d = A**2+B**2
print(math.sqrt(A*A/d), math.sqrt(B*B/d))
