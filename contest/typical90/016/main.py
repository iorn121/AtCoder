N = int(input())
# coins = list(map(int, input().split()))

# coins.sort(reverse=True)

ans = 10**9
# for i in range(N//coins[0]+1):
#     for j in range((N-coins[0]*i)//coins[1]+1):
#         rest = N-i*coins[0]-j*coins[1]
#         if rest % coins[2] == 0:
#             ans = min(ans, i+j+rest // coins[2])

A,B,C=reversed(sorted(map(int, input().split())))

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = gcd(b, a % b)
    y -= a//b*x
    return g, x, y

g,x,y=gcd(b,c)

for i in range(10000):
    

print(ans)
