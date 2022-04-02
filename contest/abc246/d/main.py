N = int(input())
for a in range(10**6+1):
    if a*a*a*4 < N:
        continue
    for b in range(a+1):
        x = a*a*a+a*a*b+a*b*b+b*b*b
        if N <= x or x >= 10**18:
            print(min(x, 10**18))
            exit()
