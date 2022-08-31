import bisect
import imp


N, K = map(int, input().split())
P = list(map(int, input().split()))

front = [0]
field = [[]]
num = [0]
ans = [-1]*N
for i, p in enumerate(P):
    if front[-1] < p:
        if K == 1:
            ans[p-1] = i+1
        else:
            front.append(p)
            field.append([p])
            num.append(1)
    else:
        j = bisect.bisect_left(front, p)
        field[j].append(p)
        num[j] += 1
        front[j] = p
        if num[j] == K:
            for card in field[j]:
                ans[card-1] = i+1
            front.pop(j)
            field.pop(j)
            num.pop(j)
print(*ans, sep='\n')
