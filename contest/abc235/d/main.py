from collections import deque
A, N = map(int, input().split())

M = 1
while M <= N:
    M *= 10

que = deque()
que.append(1)
d = [-1]*M
d[1] = 0

while que:
    num = que.popleft()
    dnum = d[num]
    num_a = num*A
    if num_a < M and d[num_a] == -1:
        que.append(num_a)
        d[num_a] = dnum+1

    if num > 9 and num % 10 != 0:
        s = str(num)
        num_s = int(s[-1]+s[:-1])
        if num_s < M and d[num_s] == -1:
            que.append(num_s)
            d[num_s] = dnum+1

print(d[N])
