import itertools


def embed(axis, menseki):
    canDo = True
    newXY = []
    if len(axis) == 0:
        canDo = False
        return canDo, newXY
    for i in axis:
        axisX = i[0]
        axisY = i[1]
        print(axisX, axisY)
        if axisX*axisY > menseki:
            canDo = False
            return canDo, newXY
        for j in range(reversed(range(1, axisX))):
            if menseki % j == 0 and menseki/j <= axisY:
                Y = menseki//j
                newXY.append((axisX, axisY-Y))
                continue
        for j in range(reversed(range(1, axisY))):
            if menseki % j == 0 and menseki/j <= axisX:
                X = menseki//j
                newXY.append((axisX-X, axisY))
                continue
        if len(newXY) == 0:
            canDo = False

    return canDo, newXY


default = list(map(int, input().split()))

XY = default[:2]
iters = list(itertools.permutations(default[2:]))
canDo = []

for i in range(6):
    testXY = [XY[:]]
    for j in range(3):
        print(testXY, iters[i][j])
        can, testXY = embed(testXY, iters[i][j])
        canDo.append(can)

print("Yes" if True in canDo else "No")
