L,R = map(int, input().split())

def count_sneak_numbers(N):
    cnt=0
    d=len(str(N))
    for i in range(d):
        for j in range(1,10):
            cnt+=j**i
    top = int(str(N)[0])
    for i in range(1,top):
        cnt+=(i-1)**(d-1)
    

count_sneak_numbers(R)