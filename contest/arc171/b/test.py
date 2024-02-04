from p import main,another
import itertools

N=5
for i in itertools.product(range(1, N+1), repeat=N):
    print(i)
    x=list(i)
    a=main(N,x)
    b=another(N,x)
    # print(a,b)
    print("Yes" if a==b else "No")
    if a!=b:
        print("No")
        print(a,b)
        break
    