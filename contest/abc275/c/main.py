S=[input() for _ in range(9)]
pones=[]
for i in range(9):
    for j in range(9):
        if S[i][j] =="#":
            pones.append([i,j])
N=len(pones)
if N<4:
    exit(print(0))

cnt=0
for i in range(N-3):
    for j in range(i+1,N-2):
        for k in range(j+1,N-1):
            for l in range(k+1,N):
                [dy,dx]=[pones[i][q]-pones[j][q] for q in range(2)]
                [dy2,dx2]=[pones[k][q]-pones[l][q] for q in range(2)]
                [dy3,dx3]=[pones[i][q]-pones[k][q] for q in range(2)]

                if( dy*dx2==dy2*dx and abs(dy)==abs(dy2) and abs(dx)==abs(dx2))and(dy**2+dx**2==dy3**2+dx3**2)and(dy*dy3+dx*dx3==0):
                    # print(pones[i])
                    # print(pones[j])
                    # print(pones[k])
                    # print(pones[l])
                    cnt+=1
                    # print("----------")

print(cnt)