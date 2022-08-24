R,C = map(int, input().split())
print("black" if max(abs(8-R),abs(8-C))%2==1 else "white")