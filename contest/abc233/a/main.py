X, Y = map(int, input().split())

ans = (Y-X+9)//10 if Y > X else 0

print(ans)
