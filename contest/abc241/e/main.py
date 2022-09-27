N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = 0
cnt = 0
loop_before = []
loop_A = [A[0]]
index = [-1]*N
index[0] = cnt
start = 0
loop_n = 0
while True:
    cnt += 1
    tmp += loop_A[-1]
    tmp %= N
    if index[tmp] == -1:
        loop_A.append(A[tmp])
        index[tmp] = cnt
    else:
        start = index[tmp]
        loop_before = loop_A[:start]
        loop_A = loop_A[start:]
        loop_n = cnt-start
        break
# print(loop_before)
# print(loop_A)
# print(start, loop_n)
if K < start:
    print(sum(loop_before[:K]))
else:
    ans = sum(loop_before)
    # print(ans)
    K -= start
    n = K//loop_n
    x = K % loop_n
    # print(n, x)
    ans += sum(loop_A)*n+sum(loop_A[:x])
    print(ans)
