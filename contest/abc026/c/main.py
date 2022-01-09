N = int(input())
boss = {i: [] for i in range(1, N+1)}
money = [0]*(N+1)
for i in range(2, N+1):
    b = int(input())
    boss[b].append(i)

for i in range(N, 0, -1):
    if boss[i]:
        m = [money[d] for d in boss[i]]
        money[i] = max(m)+min(m)+1
    else:
        money[i] = 1

print(money[1])
