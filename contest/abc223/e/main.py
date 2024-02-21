X,Y,A,B,C=map(int,input().split())

def check(w,h,area):
    if w*h>=area:
        return w,h-(area+w-1)//w
    else:
        return -1,-1

def solve_all(nX,nY):
    nA,nB,nC=A,B,C
    nX,nY=check(nX,nY,nA)
    nX,nY=check(nX,nY,nB)
    nX,nY=check(nX,nY,nC)
    if nX==-1:
        return
    else:
        print("Yes")
        exit()

def solve(nX,nY,nA,nB,nC):
    nY,nX=check(nX,nY,nA)
    nX,nY=check(nX,nY,nB)
    nX,nY=check(nX,nY,nC)
    if nX==-1:
        return
    else:
        print("Yes")
        exit()

solve_all(X,Y)
solve_all(Y,X)
solve(X,Y,A,B,C)
solve(Y,X,A,B,C)
solve(X,Y,B,A,C)
solve(Y,X,B,A,C)
solve(X,Y,A,C,B)
solve(Y,X,A,C,B)
solve(X,Y,C,A,B)
solve(Y,X,C,A,B)
solve(X,Y,B,C,A)
solve(Y,X,B,C,A)
solve(X,Y,C,B,A)
solve(Y,X,C,B,A)


print("No")

