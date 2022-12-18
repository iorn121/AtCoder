N,X,Y= map(int, input().split())
A= list(map(int, input().split()))

sx=A[0]
sy=0
Ax=A[0::2]
Ay=A[1::2]
xt=sum(Ax)
yt=sum(Ay)

if X<0:
    X=-X+sx*2
if Y<0:
    Y=-Y
mx=(xt-X)//2
my=(yt-Y)//2
# print(xt,yt)
# print(mx,my)
if mx<0 or my<0:
    exit(print("No"))
if (xt-X)%2!=0 or (yt-Y)%2!=0:
    exit(print("No"))
    
dpx=[False]*(mx+1)
dpx[0]=True
dpy=[False]*(my+1)
dpy[0]=True
for a in Ax[1:]:
    for i in range(mx):
        if a+i<=mx and dpx[i]:
            dpx[a+i]=True
for a in Ay:
    for i in range(my):
        if a+i<=my and dpy[i]:
            dpy[a+i]=True
# print(dpx)
# print(dpy)
print("Yes" if dpx[mx] and dpy[my] else "No")
