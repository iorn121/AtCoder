C = int(input())
d = [0, 0, 0]
for i in range(C):
    N = list(map(int, input().split()))
    N.sort()
    for j in range(3):
        d[j] = max(d[j], N[j])

print(d[0]*d[1]*d[2])
