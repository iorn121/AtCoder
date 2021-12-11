from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]
d = defaultdict(int)
for i in range(N):
    d[S[i]] += 1

ans = ""
max_num = 0
for k, v in d.items():
    if max_num < v:
        ans = k
        max_num = v

print(ans)
