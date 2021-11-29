N, K = map(int, input().split())

A = list(map(int, input().split()))

num_list = []

for i in range(N):
    num_list.append((A[i], i))

num_list.sort()

ans = [0]*N

X = K//N
K %= N

for i in range(N):
    ans[num_list[i][1]] = X
    if i < K:
        ans[num_list[i][1]] += 1

for i in range(N):
    print(ans[i])
