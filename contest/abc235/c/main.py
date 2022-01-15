from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
num_list = defaultdict(int)
for i, a in enumerate(A):
    num_list[a] += 1
    d[str(a)+':'+str(num_list[a])] = i+1

for i in range(Q):
    x, k = map(int, input().split())
    num = d[str(x)+':'+str(k)]
    if num == 0:
        print(-1)
    else:
        print(num)
