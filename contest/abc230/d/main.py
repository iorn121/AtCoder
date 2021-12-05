N, D = map(int, input().split())
walls = []

for i in range(N):
    L, R = map(int, input().split())
    walls.append((L, R))

walls.sort(key=lambda x: x[1])

ans = 0
x = -1 << 40

for l, r in walls:
    if x+D-1 < l:
        ans += 1
        x = r

print(ans)
