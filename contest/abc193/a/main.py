from decimal import Decimal
A, B = map(Decimal, input().split())
print((A-B)/A*100)
