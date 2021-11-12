S = input()

N = len(S)

left = S[0]

sList = []
up = 0
down = 0
ans = 0


def keisan(x):
    if x == 0:
        return 0
    ans = (x+1)*x//2
    return ans


for i in range(N):
    if S[i] == "<":
        if down != 0:
            sList.append((up, down))
            up = 0
            down = 0
        up += 1
    else:
        down += 1

sList.append((up, down))

for up, down in sList:
    large = max(up, down)
    small = min(up, down)
    ans += keisan(large)+keisan(small-1)

print(ans)
