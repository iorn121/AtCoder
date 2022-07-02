N, Q, X = map(int, input().split())
W = list(map(int, input().split()))
capacity = [0]*N
# capacity[i] i番目からじゃがいも入れたとき何個まで入れられるか

# 尺取り
total = sum(W)
cycle = X//total
X -= cycle*total
now = 0
index = 0
for i in range(2*N):
    now += W[i % N]
    # print(f"i: {i}")
    if index >= N:
        break
    while now >= X:
        capacity[index] = cycle*N+i+1-index
        # print(f"index: {index}")
        # print(f"cap[{index}]: {capacity[index]}")
        now -= W[index]
        index += 1
        if index >= N:
            break

# print(capacity)


start = 0
tmp = [-1]*N
ans = []
tans = 0
l = 0
loop = 0
sloop = 0
while 1:
    if tmp[start] != -1:
        loop = l-tmp[start]
        sloop = tmp[start]
        break
    ans.append(capacity[start])
    tans += ans[-1]
    tmp[start] = l
    l += 1
    start = (tans) % N
# print(sloop, loop, ans)
for _ in range(Q):
    k = int(input())
    k -= 1
    if k > sloop:
        k = (k-sloop) % loop+sloop
    print(ans[k])
