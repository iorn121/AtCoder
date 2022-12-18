from decimal import Decimal

A,B=map(Decimal, input().split())
ans=B/A
print(ans.quantize(Decimal("1e-3")))