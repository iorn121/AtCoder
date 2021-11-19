A, B = map(int, input().split())
ans = "Alloy"
if A == 0:
    ans = "Silver"
elif B == 0:
    ans = "Gold"
print(ans)
