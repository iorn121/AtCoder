N,M= map(int, input().split())
A= list(map(int, input().split()))
phase=[set() for _ in range(M)]

for i,a in enumerate(A,1):
    
    s=max(0,(-a-1)//i)
    t=min(M,(N-a-1)//i)
    # print("i",i,"a",a)
    # print(s,t)

    for j in range(s,t):
        phase[j].add(a+i*(j+1))

for s in phase:
    for i in range(N+1):
        if i not in s:
            print(i)
            break