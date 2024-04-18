N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
OP = [list(map(int,input().split())) for _ in range(M)]
Q = int(input())
AB = [list(map(int,input().split())) for _ in range(Q)]

def MatMul(a,b):
    return [[sum([axz*byz for (axz,byz) in zip(ax,by)]) for by in zip(*b)] for ax in a]


def main():
    mattemp = [[1,0,0],[0,1,0],[0,0,1]]
    Mat = [mattemp]

    for i in range(M):
        com = OP[i][0]
        if com == 1:
            mat1 = [[0,-1,0],[1,0,0],[0,0,1]]
            mattemp = MatMul(mattemp,mat1)
        elif com == 2:
            mat2 = [[0,1,0],[-1,0,0],[0,0,1]]
            mattemp = MatMul(mattemp,mat2)
        elif com == 3:
            p=OP[i][1]
            mat3 = [[-1,0,0],[0,1,0],[2*p,0,1]]
            mattemp = MatMul(mattemp,mat3)
        elif com == 4:
            p=OP[i][1]
            mat4 = [[1,0,0],[0,-1,0],[0,2*p,1]]
            mattemp = MatMul(mattemp,mat4)
        Mat.append(mattemp)
    for i in range(Q):
        a,b = AB[i]
        x,y = XY[b-1]
        mxy = [[x,y,1] for _ in range(3)]
        mattemp = MatMul(mxy,Mat[a])
        print(mattemp[0][0],mattemp[0][1])
main()