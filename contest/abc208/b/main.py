P = int(input())

coin = []


def kaijou(x):
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans


for i in range(1, 11):
    coin.append(kaijou(i))

coin.reverse()
ans = 0
for i in range(10):
    if P >= coin[i]:
        ans += P//coin[i]
        P %= coin[i]

print(ans)
