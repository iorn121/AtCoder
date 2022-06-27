h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
if h1+h2+h3 == w1+w2+w3:
    for x1 in range(1, w1-1):
        for x2 in range(1, w1-x1):
            for y1 in range(1, w2-1):
                for y2 in range(1, w2-y1):
                    z1 = h1-x1-y1
                    x3 = w1-x1-x2
                    y3 = w2-y1-y2
                    z2 = h2-x2-y2
                    z3 = h3-x3-y3
                    if z1 > 0 and x3 > 0 and y3 > 0 and z2 > 0 and z3 > 0:
                        ans += 1
print(ans)
