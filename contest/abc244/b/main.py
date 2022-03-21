N = int(input())
T = input()
direction = [
    (1, 0), (0, -1), (-1, 0), (0, 1)
]
x, y = 0, 0
d = 0
for t in T:
    if t == 'S':
        x += direction[d][0]
        y += direction[d][1]
    else:
        d = (d+1) % 4

print(x, y)
