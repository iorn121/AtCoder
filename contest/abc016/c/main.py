N, M = map(int, input().split())
friends = [[]for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    friends[A].append(B)
    friends[B].append(A)

for i in range(N):
    cnt = 0
    check = [True]*N
    for j in friends[i]:
        for k in friends[j]:
            if check[k] and k != i and k not in friends[i]:
                check[k] = False
                cnt += 1
    print(cnt)
