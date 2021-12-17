N = int(input())
xyh = []
for i in range(N):
    x, y, h = map(int, input().split())
    xyh.append((x, y, h))
for cx in range(101):
    for cy in range(101):
        ch = 1
        flg = True
        for i in range(N):
            x, y, h = xyh[i]
            if h != 0:
                ch = h+abs(cx-x)+abs(cy-y)
        for i in range(N):
            x, y, h = xyh[i]
            if h != max(ch-abs(cx-x)-abs(cy-y), 0):
                flg = False
                break
        if flg:
            print(cx, cy, ch)
