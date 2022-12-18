N,M=map(int, input().split())
A=list(map(int,input().split()))

def change_order(a,b):
    if a<b:
        return (a,b)
    else:
        return (b,a)


B=[i+1 for i in range(N)]
change=[]
for i,a in enumerate(A):
    a-=1
    change.append(change_order(B[a], B[a+1]))
    B[a],B[a+1]=B[a+1],B[a]

convertB={}
for i,b in enumerate(B):
    convertB[b]=i+1
# print(convertB)
for i in range(M):
    if change[i][0]==1:
        print(convertB[change[i][1]])
    else:
        print(convertB[1])