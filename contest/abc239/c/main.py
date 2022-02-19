x1, y1, x2, y2 = map(int, input().split())

dxy = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]

new1 = set()
new2 = set()
for i in range(8):
    new1.add((x1+dxy[i][0], y1+dxy[i][1]))
    new2.add((x2+dxy[i][0], y2+dxy[i][1]))

print('Yes' if len(new1 & new2) > 0 else 'No')
