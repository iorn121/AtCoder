N, K = map(int, input().split())

l = []

for i in range(N):
    a, b = map(int, input().split())
    l.append((a, b))

l.sort()

for i in range(N):
    a, b = l[i]
    if b >= K:
        print(a)
        exit()
    else:
        K -= b
