from collections import defaultdict
S = input()
ans = 0
use = set()
can_use = set()

for i in range(10):
    if S[i] == "o":
        use.add(str(i))
        can_use.add(str(i))
    elif S[i] == "?":
        can_use.add(str(i))
for i in range(10000):
    num = str(i).zfill(4)
    num_use = set()
    for j in range(4):
        num_use.add(num[j])
    if num_use <= can_use and use <= num_use:
        ans += 1


print(ans)
