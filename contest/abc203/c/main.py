N, K = map(int, input().split())
friends = []
for i in range(N):
    A, B = map(int, input().split())
    friends.append((A, B))

friends.sort()

now = 0
for i in range(N):
    if now+K < friends[i][0]:
        print(now+K)
        exit()
    else:
        K = now+K-friends[i][0]+friends[i][1]
        now = friends[i][0]

print(now+K)
