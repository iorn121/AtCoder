cx, cy, r = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())

rec_xy = [(sx, sy), (sx, ey), (ex, sy), (ex, ey)]

outside = False
inside = False
cnt = 0
for x, y in rec_xy:
    total = (cx-x)**2+(cy-y)**2
    if total <= r*r:
        cnt += 1
if cnt == 4:
    inside = True

if sx+r <= cx <= ex-r and sy+r <= cy <= ey-r:
    outside = True
print('NO' if outside else 'YES')
print('NO' if inside else 'YES')
