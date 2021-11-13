import math

N = int(input())
S = list(map(int, input().split()))


def warizan(x):
    for i in range(7, int(math.sqrt(x)+1), 4):
        if x % i == 0 and ((x//i)-3) % 4 == 0:
            return 0
    return 1


ans = 0
for i in range(len(S)):
    X = S[i]*4+9
    ans += warizan(X)

print(ans)
